import json
import luigi
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
