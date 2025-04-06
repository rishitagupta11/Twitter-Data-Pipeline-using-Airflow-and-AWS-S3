# Twitter-Data-Pipeline-using-Airflow-and-AWS-S3

# Twitter ETL Project

This is a simple ETL (Extract, Transform, Load) project that collects tweets from Elon Musk's Twitter account using the Twitter API and stores them in a CSV file. The ETL process is automated using Apache Airflow.

## Features
- Extracts tweets using Tweepy (Twitter API)
- Transforms tweet data (text, likes, retweets, timestamp)
- Loads data into a CSV file
- Scheduled daily using Apache Airflow

## Setup

### 1. Install Dependencies
Run the setup script:
```bash
chmod +x twitter_commands.sh
./twitter_commands.sh
```

### 2. Set Twitter API Keys
Create a `.env` file with your Twitter API credentials:
```env
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

### 3. Run Airflow
```bash
airflow db init
airflow webserver --port 8080
airflow scheduler
```
Place the scripts in your Airflow DAGs folder. Enable the DAG from the Airflow UI.

## Files
- `twitter_etl.py`: ETL logic
- `twitter_dag.py`: Airflow DAG definition
- `twitter_commands.sh`: Dependency setup script
- `elonmusk_twitter_data.csv`: Output CSV


