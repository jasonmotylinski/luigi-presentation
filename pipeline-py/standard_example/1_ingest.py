import json
from nfl import scraper


print json.dumps(scraper.scrape_category("PASSING"), indent=2)
