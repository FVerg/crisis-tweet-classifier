import pandas as pd

# This function takes in input:
# - list_tweets: A list of dictionaries, containing tweet info (Needs to have TweetID attirbute)
# - filename: Name of the csv file that's going to contain the tweets and infos


def tweets_to_csv(list_tweets, filename):
    df = pd.DataFrame(list_tweets)
    df = df.set_index("TweetID")
    col_names = list(df.columns.values)
    df.to_csv(filename, header=col_names, index=True, sep=',', mode='w')
