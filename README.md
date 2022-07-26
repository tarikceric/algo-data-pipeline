# algo-data-pipeline

A data ETL pipeline that loads Algorand DEX data into a data warehouse at a set interval, in order to power a Metabase dashboard. Inspiration from [bitcoin monitor project](https://startdataengineering.com/post/data-engineering-project-to-impress-hiring-managers/).

# Overview
![Screenshot](https://github.com/tarikceric/algo-data-pipeline/blob/main/images/pipeline-arch.png)


1. Data is pulled from the [Vestige API](https://free-api.vestige.fi/providers) and loaded into the warehouse via [exchange_etl.py](https://github.com/tarikceric/algo-data-pipeline/blob/main/src/algopipeline/exchange_etl.py)
2. Docker containers are used for Postgres database and Metabase dashboard
    - warehouse connection credentials are stored as env variables within the docker compose definition
3. The ETL script is scheduled to run every 5 minutes via a cron job
4. Production: Data pipelines and dashboards are ran as containers on an EC2 Instance

![Screenshot_vol](https://github.com/tarikceric/algo-data-pipeline/blob/main/images/dex_volumes.png) ![Screenshot_tvl](https://github.com/tarikceric/algo-data-pipeline/blob/main/images/dex_tvls.png)



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
git clone https://github.com/tarikceric/algo-data-pipeline.git
cd algo-data-pipeline
```
To test locally:
```
docker compose --env-file env up --build -d
```

To deploy to Production:
1. Create an EC2 instance in your AWS UI -> add a TCP rule on port 3000 that accepts inbound connections from any 0.0.0.0/0 address
2. Create/download a pem file if necessary
3. Deploy code to Ec2 via:
```
cd algo-data-pipeline
chmod 755 ./deploy_helpers/send_code_to_prod.sh
chmod 400 your-pem-file-full-location
./deploy_helpers/send_code_to_prod.sh your-pem-file-full-location your-EC2-Public-DNS
```
4. Install docker and start ETL/dashboard containers on Ec2:

```
chmod 755 install_docker.sh
./install_docker.sh
# verify that docker and docker compose installed
docker --version
docker-compose --version

# start the containers
unzip algo-data-pipeline.gzip && cd algo-data-pipeline/
docker-compose --env-file env up --build -d
```

5. Log into your remote Metabase instance by using http://your-public-ipv4-address:3000
6. In Metabase, set up connection to the Postgres warehouse with same credentials as used throughout
