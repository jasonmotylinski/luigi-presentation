import elasticsearch
import json
import luigi

from elasticsearch.helpers import bulk
from luigi.contrib import esindex
from nfl import scraper


class IngestData(luigi.Task):

    category = luigi.Parameter()

    def output(self):
        target = luigi.LocalTarget("output/{0}.json".format(self.category))
        target.category = self.category
        return target

    def run(self):
        with self.output().open('w') as f:
            f.write(json.dumps(scraper.scrape_category(self.category), indent=2))


class GenerateReport(luigi.Task):

    def requires(self):
        for c in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
            yield IngestData(c)

    def output(self):
        return luigi.LocalTarget("output/report.json")

    def run(self):
        report = {}

        for inputFile in self.input():
            with inputFile.open('r') as f:
                data = json.loads(f.read())
                report[inputFile.category] = data[:-10]

        with self.output().open('w') as f:
            for k in report.keys():
                for el in report[k]:
                    f.write(el.values()[0] + "," + el.values()[1] + "," + el.values()[2] + "," + el.values()[3] + '\n')


class ExportToES(luigi.Task):

    def __init__(self):
        self.host = "localhost"
        self.port = "9200"
        self.index = "nfl"
        super(ExportToES, self).__init__()

    def _init_connection(self):
        return elasticsearch.Elasticsearch(
            host=self.host,
            port=self.port
        )

    def requires(self):
        for c in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
            yield IngestData(c)

    def output(self):
        return esindex.ElasticsearchTarget(host=self.host, port=self.port, index=self.index, doc_type="report", update_id="_id")

    def docs(self):
        for inputFile in self.input():
            with inputFile.open('r') as f:
                for element in json.loads(f.read()):
                    element["_type"] = inputFile.category
                    element["_index"] = self.index
                    yield element

    def run(self):
        es = self._init_connection()
        bulk(es, self.docs())
        self.output().touch()
