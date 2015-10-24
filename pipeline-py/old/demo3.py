import json
import os

from nfl import scraper

if not os.path.isdir("output"):
    os.makedirs("output")

for category in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
    with open('output/{0}.json'.format(category), 'wt') as f:
        f.write(json.dumps(scraper.scrape_category(category), indent=2))

print "Complete!"
