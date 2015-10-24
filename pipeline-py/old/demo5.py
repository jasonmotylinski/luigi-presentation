import json
import os

from nfl import scraper

for year in range(2000, 2015):
    path = "output/{0}".format(year)
    if not os.path.isdir(path):
        os.makedirs(path)

    report = {}

    for category in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
        with open('{0}/{1}.json'.format(path, category), 'wt') as f:
            data = scraper.scrape_category(category)
            f.write(json.dumps(data, indent=2))
            report[category] = data[:-10]

    with open('{0}/report.json'.format(path), 'wt') as f:
        for k in report.keys():
            for el in report[k]:
                f.write(el.values()[0] + "," + el.values()[1] + "," + el.values()[2] + "," + el.values()[3] + '\n')

print 'Complete!'
