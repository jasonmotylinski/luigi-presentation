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


class GenerateAll(luigi.Task):

    def requires(self):
        for c in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
            yield IngestData(c)
