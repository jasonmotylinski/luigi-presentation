1. Pre-presentation
 1. re-initialize elasticsearch
 1. clear out venv
1. Demo old
 1. Explain nfl lib https://github.com/jasonmotylinski/nfl which scrapes these web pages http://www.nfl.com/stats/categorystats?tabSeq=0&statisticCategory=PASSING&season=2015&seasonType=REG
 1. virtualenv venv
 1. source venv/bin/activate
 1. cd standardpipeline
 1. pip install -r requirements
 1. python 1_ingest.py
 1. Clear output
 1. python 2_ingest.py
 1. Clear output
 1. python 3_ingest.py
 1. Clear output
 1. python 4_ingest.py
 1. Clear output
1. STOP - Go back to slides
1. Demo new
 1. pip install luigi
 1. Clear output
 1. luigi --module luigipipeline.1_steps IngestData
 1. luigi --module luigipipeline.2_steps IngestData
 1. luigi --module luigipipeline.3_steps IngestData