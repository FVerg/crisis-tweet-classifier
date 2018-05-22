import pandas as pd

# This function takes in input:
# - list_tweets: A list of dictionaries, containing tweet info (Needs to have TweetID attirbute)
# - filename: Name of the csv file that's going to contain the tweets and infos


def tweets_to_csv(list_tweets, filename):
    df = pd.DataFrame(list_tweets)
    df = df.set_index("TweetID")
    col_names = list(df.columns.values)
    df.to_csv(filename, header=col_names, index=True, sep=',', mode='w')


# Input:
# - input_file: File containing a tag for each line
# Output:
# - List containing tags stored in the input file
def get_tagset(input_file):
    tagset = []
    tagset_file = open(input_file, 'r')
    for line in tagset_file:
        tagset.append(line.replace("\n", "").strip())

    return tagset
# print(tagset)
