import twython
from twython import Twython
import pandas as pd
import json
import numpy as np

from user_age import user_age
from is_geotagged import is_geotagged

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

list_infos = []             # List that will contain the new informations

# Access to the informations of each tweet, retrieving them through Tweet ID
correctly_extracted = 0
not_available = 0
for id in tweet_ids:
    try:
        tweet = twitter.show_status(id=id)
        list_infos.append({"Username": tweet['user']['name'],
                           "TweetID": id, "Followers": tweet['user']['followers_count'],
                           "Followed": tweet['user']['friends_count'], "TwitterAge": user_age(tweet['user']['created_at']),
                           "TotalTweets": tweet['user']['statuses_count'], "Verified": tweet['user']['verified'],
                           "Geotagged": is_geotagged(tweet), "nHashtags": len(tweet['entities']['hashtags']), "nURLs": len(tweet['entities']['urls']),
                           "nMentions": len(tweet['entities']['user_mentions'])})
        correctly_extracted = correctly_extracted + 1
        print("[DEBUG] Found info for tweet: ", id, ". Added to list.")
    except twython.exceptions.TwythonRateLimitError as e:
        print(e)
        print("DEBUG] Try again in some minutes, reached max number of tweets")
        print("[DEBUG] ", correctly_extracted, " tweets have been correctly extracted")
        print("[DEBUG] ", not_available, " tweets have encountered problems in being downloaded")
        break
    except twython.exceptions.TwythonError as e:
        print(e)    # If an exception occurs (APIs return an unexpected HTTP response code) we print it
        not_available = not_available + 1
'''
        list_infos.append({"Username": None, "ID": id, "Followers": None,
                           "Followed": None, "TwitterAge": None, "TotalTweets": None, "Verified": None,
                           "Geotagged": None, "nHashtags": None, "nURLs": None, "nMentions": None})
'''
meta_tweets = pd.DataFrame(list_infos)
meta_tweets = meta_tweets.set_index('TweetID')

col_names = list(meta_tweets.columns.values)
meta_tweets.to_csv(r'metatweets.csv', header=col_names, index=True, sep=',', mode='a')
