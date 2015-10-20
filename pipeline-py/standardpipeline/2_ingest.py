import json
from nfl import scraper


with open('../output/passing.json', 'wt') as f:
    f.write(json.dumps(scraper.scrape_category("PASSING"), indent=2))

print "Complete!"
