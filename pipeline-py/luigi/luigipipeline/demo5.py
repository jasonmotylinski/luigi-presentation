import elasticsearch
import json
import luigi

from elasticsearch.helpers import bulk
from luigi.contrib import esindex
from nfl import scraper


class IngestData(luigi.Task):

    category = luigi.Parameter()
    year = luigi.Parameter()

    def output(self):
        target = luigi.LocalTarget("output/{0}/{1}.json".format(self.year, self.category))
        target.category = self.category
        target.year = self.year
        return target

    def run(self):
        with self.output().open('w') as f:
            f.write(json.dumps(scraper.scrape_year_category(self.year, self.category), indent=2))


class ExportToES(luigi.Task):

    def __init__(self):
        self.host = "localhost"
        self.port = "9200"
        self.index = "demo5"
        super(ExportToES, self).__init__()

    def _init_connection(self):
        return elasticsearch.Elasticsearch(
            host=self.host,
            port=self.port
        )

    def requires(self):
        for year in range(2000, 2015):
            for c in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
                yield IngestData(c, year)

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
