import json
import luigi
from nfl import scraper


class IngestData(luigi.Task):

    def output(self):
        return luigi.LocalTarget("output/passing.json")

    def run(self):
        with self.output().open('w') as f:
            f.write(json.dumps(scraper.scrape_category("PASSING"), indent=2))


class GenerateAll(luigi.Task):

    def requires(self):
        for c in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
            yield IngestData(c)
