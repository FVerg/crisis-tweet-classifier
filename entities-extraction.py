import nltk
import pandas as pd

pd.options.mode.chained_assignment = None

def pos_tweet(tweet):
    pos = nltk.sent_tokenize(tweet)
    pos = [nltk.word_tokenize(sent) for sent in pos]
    pos = [nltk.pos_tag(sent) for sent in pos]
    return pos


dataset = pd.read_csv('C:/dataset/2013_pakistan_eq.csv', header=0)


dataset.set_index('tweet_id')

tweet_ids = dataset['tweet_id']
tweet_texts = dataset['tweet_text']

for i in range(0, tweet_ids.size):
    tweet_ids[i] = tweet_ids[i].replace("'", "")

tagged_tweets = []

for id, text in zip(tweet_ids, tweet_texts):
    tagged_tweets.append({"TweetID": id, "Text": text, "POS": pos_tweet(text)})
