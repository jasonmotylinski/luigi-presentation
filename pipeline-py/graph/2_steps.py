import json
import luigi
from nfl import scraper


class IngestData(luigi.Task):

    def output(self):
        return luigi.LocalTarget("output/passing.json")

    def run(self):
        with self.output().open('w') as f:
            f.write(json.dumps(scraper.scrape_category("PASSING"), indent=2))


class GenerateReport(luigi.Task):

    def requires(self):
        return [IngestData()]

    def output(self):
        return luigi.LocalTarget("output/report.json")

    def run(self):
        report = {}

        for inputFile in self.input():
            with inputFile.open('r') as f:
                data = json.loads(f.read())
                report["PASSING"] = data[:-10]

        with self.output().open('w') as f:
            for k in report.keys():
                for el in report[k]:
                    f.write(el.values()[0] + "," + el.values()[1] + "," + el.values()[2] + "," + el.values()[3] + '\n')
