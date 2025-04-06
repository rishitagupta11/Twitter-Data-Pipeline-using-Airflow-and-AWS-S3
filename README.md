# Twitter-Data-Pipeline-using-Airflow-and-AWS-S3


This is a simple ETL (Extract, Transform, Load) project that collects tweets from Elon Musk's Twitter account using the Twitter API and stores them in a CSV file. The ETL process is automated using Apache Airflow.

## Features
- Extracts tweets using Tweepy (Twitter API)
- Transforms tweet data (text, likes, retweets, timestamp)
- Loads data into a CSV file
- Scheduled daily using Apache Airflow


## Files
- `twitter_etl.py`: ETL logic
- `twitter_dag.py`: Airflow DAG definition
- `twitter_commands.sh`: Dependency setup script
- `elonmusk_twitter_data.csv`: Output CSV


