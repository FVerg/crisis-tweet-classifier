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

dataset = pd.read_csv('C:/dataset/2014_california_eq.csv', header=0)
