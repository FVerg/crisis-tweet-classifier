# In this code snippet I would like to take the original dataset with original tweet texts,
# and create a new dataset containing for each tweet, the 0/1 information about the presence or
# absence of each tag available in NLP Tagger Tagset.
# The tagset is in tagset.txt

from nltk.tag.stanford import CoreNLPNERTagger
from utilities import tweets_to_csv, get_tagset

import pandas as pd

dataset = pd.read_csv('C:/dataset/2014_california_eq.csv', header=0)

# List containing all the possible tags
tagset = get_tagset("tagset.txt")
for i in range(len(tagset)):
    tagset[i] = tagset[i].lower().capitalize()

dataset = pd.read_csv('C:/dataset/2014_california_eq.csv', header=0)

tweets = []

tweet_ids = dataset["tweet_id"]
tweet_text = dataset["tweet_text"]
'''
attributes = ["TweetID", "Text"]
attributes.extend(tagset)
print(attributes)
'''
for id, text in zip(tweet_ids, tweet_text):
    filtered_text = ""
    for word in text:
        if word.startswith("#"):
            filtered_text = filtered_text + word.replace("#", "")
        else:
            filtered_text = filtered_text + word
    # Don't know how to create dictionary using some keys taken from list
    tweets.append(dict([("TweetID", id), ("Text", text)], [tag, []] for tag in tagset))
