

import tweepy

import pandas as pd

import json

from datetime import datetime

!pip install s3fs

import s3fs

access_key= ""                                #API key
access_secret= ""                             #API key secret
consumer_key= ""                              #Access Token
consumer_secret= ""                           #Access Token Secret

#Creating connection between current code and twitter API
#Twitter authentication and authorization

auth=tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#Creation of API object

api=tweepy.API(auth)

client = tweepy.Client(bearer_token='')
# First, you need the user ID for @elonmusk
user = client.get_user(username="elonmusk")
user_id = user.data.id
username = user.data.username

# Now fetch tweets from that user
tweets = client.get_users_tweets(
    id=user_id,
    max_results=100,  # max per request is 100
    tweet_fields=["created_at", "public_metrics"]
)

for tweet in tweets.data:
    print(tweet.text)

tweet_list = []

for tweet in tweets.data:
    metrics = tweet.public_metrics  #  access like & RT counts

    refined_tweet = {
        'user': username,
        'text': tweet.text,
        'favorite_count': metrics['like_count'],
        'retweet_count': metrics['retweet_count'],
        'created_at': tweet.created_at
    }

    tweet_list.append(refined_tweet)

df=pd.DataFrame(tweet_list)
df.to_csv("elonmusk_twitter_data.csv")

df



