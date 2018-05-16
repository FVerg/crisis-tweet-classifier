# This script allows to format a tweet dataset with the standard structure (Structured as it was when downloaded from AICR website)
# into the structure we used for metadata datasets:
# tweet_id -> TweetID
# text -> Text
# choose_one_category -> Label

# This way, it will be compatible with the other scripts (irrelevant_tweets)


import pandas as pd

dataset = pd.read_csv("C:/dataset/2013_pakistan_eq.csv", header=0)

# Deleting useless attributes
del dataset["_unit_id"], dataset["_golden"], dataset["_unit_state"], dataset["_trusted_judgments"], dataset[
    "_last_judgment_at"], dataset["choose_one_category:confidence"], dataset["choose_one_category_gold"]

# Changing names to the attributes according to our standard structure
dataset.columns = ["Label", "TweetID", "Text"]

# Set the index
dataset = dataset.set_index("TweetID")

# Removing duplicates
dataset = dataset[~dataset.index.duplicated(keep='first')]

col_names = list(dataset.columns.values)

# Save to csv
dataset.to_csv("C:/dataset/2013_pakistan_eq_temp.csv",
               sep=',', header=col_names, index=True, mode='w')
