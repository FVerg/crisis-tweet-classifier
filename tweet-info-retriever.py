import twython
from twython import Twython
import pandas as pd
import json
import numpy as np

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

# tweet_ids will be a Pandas.Series object
print(type(tweet_ids))

# Removing the apexes from each Tweet ID

for i in range(0, tweet_ids.size):
    tweet_ids[i] = tweet_ids[i].replace("'", "")

print("[DEBUG] Formatting tweets")

# Create a new DataFrame, initially containing just the IDs

# tweet_infos = pd.DataFrame(tweet_ids)

# List that will contain the new informations to add to the DataFrame tweet_infos

tweet_infos = {}            # Auxiliary dictionary
list_infos = []             # List that will contain the new informations

# Test for a single tweet: WORKS

'''
tweet = twitter.show_status(id=tweet_ids[0])
print(type(tweet))
print("id_str: ", tweet['id_str'])
print("user: ", tweet['user'])
print("followers: ", tweet['user']['followers_count'])
tweet_infos["ID"] = tweet['id']
tweet_infos["Followers"] = tweet['user']['followers_count']
print(tweet_infos)
list_infos.append(tweet_infos)
print(list_infos)
'''
# Access to the informations of each tweet, retrieving them through Tweet ID
# Problem 1: At the end, in list_infos:
#  - ID will always be the same
#  - Followers will always be none
# Problem 2: Twitter allows standard user only a limited number of requests in a 15 minutes time window.

# TO BE FIXED

for id in tweet_ids:
    try:
        tweet = twitter.show_status(id=id)
        # tweet_infos["ID"] = id
        # tweet_infos["Followers"] = tweet['user']['followers_count']
        list_infos.append({"Username": tweet['user']['name'],
                           "ID": id, "Followers": tweet['user']['followers_count'], "Followed": tweet['user']['friends_count']})
        print("[DEBUG] Found info for tweet: ", id, ". Added to list")
    except twython.exceptions.TwythonError as e:
        print(e)    # If an exception occurs (APIs return an unexpected HTTP response code) we print it
        # tweet_infos["ID"] = id
        # tweet_infos["Followers"] = None
        list_infos.append({"Username": None, "ID": id, "Followers": None, "Followed": None})

# df.to_csv(r'c:\data\pandas.txt', header=None, index=None, sep=' ', mode='a')
print(list_infos)
