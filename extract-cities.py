# Here we are going to use the Stanford NER Tagger in order to extract cities from Text

# To make this code work it is important to download stanford-corenlp-full-2018-02-27
# check the dependencies (CLASSPATH and STANFORD_MODELS) and execute this command on cmd:
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
# The above command has to be executed after having put yourself inside the corenlp-full-... folder

from nltk.tag.stanford import CoreNLPNERTagger
import pandas as pd

dataset = pd.read_csv('C:/dataset/2013_pakistan_eq.csv', header=0)

tweets = []

tweet_ids = dataset["tweet_id"]
tweet_text = dataset["tweet_text"]


for id, text in zip(tweet_ids, tweet_text):
    tweets.append({"TweetID": id, "Text": text, "Location": [],
                   "StateProvince": [], "Country": [], "City": []})

# Using the NER Tagger for each tweet and save:
# - Location
# - Country
# - State or province
# - City
for tweet in tweets:
    st = CoreNLPNERTagger(url='http://localhost:9000').tag(tweet["Text"].split())
    for tuple in st:
        if tuple[1] == "LOCATION":
            tweet["Location"].append(tuple[0])
        elif tuple[1] == "STATE_OR_PROVINCE":
            tweet["StateProvince"].append(tuple[0])
        elif tuple[1] == "COUNTRY":
            tweet["Country"].append(tuple[0])
        elif tuple[1] == "CITY":
            tweet["City"].append(tuple[0])

# Removing doubles

tweet["Location"] = list(set(tweet["Location"]))
tweet["StateProvince"] = list(set(tweet["StateProvince"]))
tweet["Country"] = list(set(tweet["Country"]))
tweet["City"] = list(set(tweet["City"]))

print(tweets)
