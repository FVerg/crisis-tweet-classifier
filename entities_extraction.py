from nltk.tag.stanford import CoreNLPNERTagger
from utilities import tweets_to_csv, get_tagset
import pandas as pd

dataset = pd.read_csv('C:/dataset/2014_california_eq.csv', header=0)

# List containing all the possible tags
tagset = get_tagset("tagset.txt")

dataset = pd.read_csv('C:/dataset/2014_california_eq.csv', header=0)
