import twython
from twython import Twython
import pandas as pd
import json

pd.options.mode.chained_assignment = None  # default='warn'

keys = json.load(open("keys.json"))

CONSUMER_KEY = keys['consumer_key']                 # Type your CONSUMER_KEY
CONSUMER_SECRET = keys['consumer_secret']           # Type your CONSUMER_SECRET
OAUTH_TOKEN = keys['access_token']                 # Type your OAUTH_TOKEN
OAUTH_TOKEN_SECRET = keys['access_token_secret']   # Type your OAUTH_TOKEN_SECRET

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

dataset = pd.read_csv('C:/dataset/2013_pakistan_eq.csv', header=0)

# Retrieving all tweet ids in order to use APIs to fetch all the informations we need on them

tweet_ids = dataset["tweet_id"]

print(type(tweet_ids))

# Removing the apexes from each Tweet ID

for i in range(0, tweet_ids.size):
    tweet_ids[i] = tweet_ids[i].replace("'", "")

print("[DEBUG] Formatting tweets")

# Create a new DataFrame, initially containing just the IDs

tweet_infos = pd.DataFrame(tweet_ids)

# List that will contain the new informations to add to the DataFrame tweet_infos

list = []

# Access to the informations of each tweet, retrieving them through Tweet ID
# PROBLEM: Twitter allows standard user only a limited number of requests in a 15 minutes time window.

for id in tweet_ids:
    try:
        tweet = twitter.show_status(id=id)
    except twython.exceptions.TwythonError as e:
        print(e)    # If an exception occurs (APIs return an unexpected HTTP response code) we print it
        pass        # Exception is not handled yet
    else:
        list.append(tweet['id_str'])

print(list)
