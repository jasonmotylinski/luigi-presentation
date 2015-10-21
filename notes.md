1. Pre-presentation
 1. re-initialize elasticsearch
 1. DELETE http://localhost:9200/nfl
 1. clear out venv
 1. prep terminal tabs to start luigi server
 1. Change display settings for Terminal
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
1. STOP - Go back to slides
 1. Discuss various outputs
1. Elasticsearch Demo 
 1. http://localhost:9200/_plugin/kibana3/src/index.html#/dashboard/file/guided.json
 1. luigi --module luigipipeline.4_steps IngestData
1. Server Demo
 1. Dependency Graph
 1. luigi --module luigipipeline.4_steps GenerateReport --workers 10