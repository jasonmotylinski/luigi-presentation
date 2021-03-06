import json
import luigi
from nfl import scraper


class IngestData(luigi.Task):

    def output(self):
        return luigi.LocalTarget("output/PASSING.json")

    def run(self):
        with self.output().open('w') as f:
            f.write(json.dumps(scraper.scrape_category("PASSING"), indent=2))
