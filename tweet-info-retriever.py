import twython
from twython import Twython
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# tweet = twitter.show_status(id=382813437513834497)


'''
print("User:", tweet['user'])
print("Text:", tweet['text'])
'''

dataset = pd.read_csv('C:/dataset/2013_pakistan_eq.csv', header=0)

# dataset

# Retrieving all tweet ids in order to use APIs to fetch all the informations we need on them
tweet_ids = dataset["tweet_id"]
tweet_ids.rename("ID")

print(type(tweet_ids))

# type(tweet_ids)

# print(tweet_ids.size)

for i in range(0, tweet_ids.size):
    tweet_ids[i] = tweet_ids[i].replace("'", "")

print("Tweet ids have been correctly formatted")

# print(tweet_ids)

tweet_infos = pd.DataFrame(tweet_ids)
list = []


for id in tweet_ids:
    try:
        tweet = twitter.show_status(id=id)
    except twython.exceptions.TwythonError as e:
        print(e)
        pass
    else:
        list.append(tweet['id_str'])
 #    tweet_infos.append(tweet['id_str'])

print(list)
