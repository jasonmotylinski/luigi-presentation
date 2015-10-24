import json
import os

from nfl import scraper

if not os.path.isdir("output"):
    os.makedirs("output")

with open('output/PASSING.json', 'wt') as f:
    f.write(json.dumps(scraper.scrape_category("PASSING"), indent=2))

print "Complete!"
