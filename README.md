# algo-data-pipeline

A data ETL pipeline that loads Algorand DEX data into a data warehouse at a set interval, in order to power a Metabase dashboard. Inspiration from [bitcoin monitor project](https://startdataengineering.com/post/data-engineering-project-to-impress-hiring-managers/).

# Overview

1. Data is pulled from the [Vestige API](https://free-api.vestige.fi/providers) and loaded into the warehouse via [exchange_etl.py](https://github.com/tarikceric/algo-data-pipeline/blob/main/src/algopipeline/exchange_etl.py)
2. Docker containers are used for Postgres database and Metabase dashboard
3. 

# Tools
- Python
- Docker
- AWS EC2



# Setup: 
The following are required:
- Docker and Docker Compose v1.27.0 or later.
- AWS account.
- AWS CLI installed and configured.
- git.

First, clone the code and cd into the project:
```
git clone https://github.com/josephmachado/bitcoinMonitor.git
cd bitcoinMonitor
```
To test locally:
```
docker compose --env-file env up --build -d
```

To deploy to Production






# Overview

## ETL Code:
