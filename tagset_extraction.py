# To make this code work it is important to download stanford-corenlp-full-2018-02-27
# check the dependencies (CLASSPATH and STANFORD_MODELS) and execute this command on cmd:
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
# The above command has to be executed after having put yourself inside the corenlp-full-... folder
# A batch file (runServer.bat) for Windows is included in the repository, to
# easily execute the server. (It has to be placed in corenlp-full-... folder)

# This code snippet takes a dataset containing text of tweets and extracts
# all the possible tags the NLP NER Tagger could extract from them.

from nltk.tag.stanford import CoreNLPNERTagger
from utilities import tweets_to_csv
import pandas as pd

dataset = pd.read_csv('C:/dataset/2014_california_eq.csv', header=0)

tweets = []

tweet_ids = dataset["tweet_id"]
tweet_text = dataset["tweet_text"]

tagset = []

for id, text in zip(tweet_ids, tweet_text):
    filtered_text = ""
    for word in text:
        if word.startswith("#"):
            filtered_text = filtered_text + word.replace("#", "")
        else:
            filtered_text = filtered_text + word

    tweets.append({"TweetID": id, "Text": filtered_text})

tagset_file = open("tagset.txt", 'w')

for tweet in tweets:
    st = CoreNLPNERTagger(url='http://localhost:9000').tag(tweet["Text"].split())

    for tuple in st:
        tagset.append(tuple[1])
        tagset = list(set(tagset))

for tag in tagset:
    tagset_file.write("%s\n" % tag)
