import twython
from twython import Twython
import pandas as pd
import json
import numpy as np
import time
import datetime as dt

from user_age import user_age
from is_geotagged import is_geotagged
from str_to_datetime import str_to_datetime

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
first_tweet_time = dt.datetime.max

for id in tweet_ids:
    while True:
        try:
            tweet = twitter.show_status(id=id)
            list_infos.append({"Username": tweet['user']['name'],
                               "TweetID": id, "Followers": tweet['user']['followers_count'],
                               "Followed": tweet['user']['friends_count'], "TwitterAge": user_age(tweet['user']['created_at']),
                               "TotalTweets": tweet['user']['statuses_count'], "Verified": tweet['user']['verified'],
                               "Geotagged": is_geotagged(tweet), "nHashtags": len(tweet['entities']['hashtags']), "nURLs": len(tweet['entities']['urls']),
                               "nMentions": len(tweet['entities']['user_mentions']), "CreationTime": tweet['created_at']})
            correctly_extracted = correctly_extracted + 1
            print("[DEBUG] Found info for tweet: ", id, ". Added to list.")

            if str_to_datetime(tweet['created_at']) < first_tweet_time:
                first_tweet_time = str_to_datetime(tweet['created_at'])
            break
        except twython.exceptions.TwythonRateLimitError as e:
            # If we reach the limit of downloadable tweets in a time window, we wait 5 minutes and try again
            print(e)
            print("[DEBUG] Maximum number of tweets reached. Trying again in 5 mins...")
            print("[DEBUG]", correctly_extracted, "tweets have been correctly extracted")
            print("[DEBUG]", not_available,
                  "tweets have encountered problems during download (403, 404, ...)")
            for i in range(300):
                if i == 299:
                    print("[DEBUG]", 300-i, "second left...")
                else:
                    print("[DEBUG]", 300-i, "seconds left...")
                time.sleep(1)
            # break
        except twython.exceptions.TwythonError as e:
            # If other exceptions occurs (APIs return an unexpected HTTP response code) we print it
            # This box includes error like 404 - Not found, 403 - User suspended etc.
            print("[DEBUG]", e)
            not_available = not_available + 1
            break
now = dt.datetime.now()

print("[DEBUG] calculating elapsed time since first tweet of the crisis")
for item in list_infos:
    creation_time = str_to_datetime(item["CreationTime"])
    delta_time = creation_time - first_tweet_time
    item["DeltaTime"] = str(delta_time)

print("[DEBUG]", correctly_extracted, "tweets have been correctly extracted")
print("[DEBUG]", not_available,
      "tweets have encountered problems during download (403, 404, ...)")


# Save tweets and their metadata into a new Dataframe
meta_tweets = pd.DataFrame(list_infos)

# Set the index (Tweet ID)
meta_tweets = meta_tweets.set_index('TweetID')

# Extract the column names from the DataFrame
col_names = list(meta_tweets.columns.values)

# Save as CSV, including header containing columns
meta_tweets.to_csv(r'metatweets3.csv', header=col_names, index=True, sep=',', mode='w')
