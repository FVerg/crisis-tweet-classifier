# The function included in this script will create a new csv file with attributes:
# - TweetID
# - hasCity (T/F): True if the tweet has a City (according with NER Tagger)
# - hasCountry (T/F): True if the tweet has a Country (according with NER Tagger)
# - hasLocation (T/F): True if the tweet has a Location (according with NER Tagger)
# - hasStateProvince:  (T/F): True if the tweet has a StateProvince (according with NER Tagger)

# It takes as input the csv containing the tagged text (eventName_eq_cities.csv)

import pandas as pd

# Specify name and path of the output file:
outputFilePath = r"C:\dataset\2013_pakistan_eq_location_tf.csv"


def has_location_infos(inputFilePath):
    dataset = pd.read_csv(inputFilePath, header=0)
    del dataset["Text"]

    # Cleaning attribute values
    dataset["TweetID"] = dataset["TweetID"].apply(remove_apexes)
    dataset["Location"] = dataset["Location"].apply(remove_apexes)
    dataset["Location"] = dataset["Location"].apply(remove_sq_brackets)
    dataset["City"] = dataset["City"].apply(remove_apexes)
    dataset["City"] = dataset["City"].apply(remove_sq_brackets)
    dataset["Country"] = dataset["Country"].apply(remove_apexes)
    dataset["Country"] = dataset["Country"].apply(remove_sq_brackets)
    dataset["StateProvince"] = dataset["StateProvince"].apply(remove_apexes)
    dataset["StateProvince"] = dataset["StateProvince"].apply(remove_sq_brackets)

    # For each record, if it has at least one location, create a new attribute hasLocation = True
    # It will be False otherwise. The same for City, StateProvince and Country
    dataset["hasLocation"] = ~(dataset["Location"] == "")
    dataset["hasCountry"] = ~(dataset["Country"] == "")
    dataset["hasCity"] = ~(dataset["City"] == "")
    dataset["hasStateProvince"] = ~(dataset["StateProvince"] == "")

    del dataset["Location"], dataset["Country"], dataset["City"], dataset["StateProvince"]

    dataset = dataset.set_index("TweetID")
    col_names = list(dataset.columns.values)

    dataset.to_csv(outputFilePath, header=col_names, index=True, sep=',', mode='w')

    print(dataset)

# This function has to be applied to datasets which have apexes encapsulating
# attribute values. E.G.: '1378129381293' and not 1378129381293
# It is used through the apply pandas function:
# dataset[Attribute] = dataset.apply(remove_apexes) -> Remove apexes to all values of Attribute column


def remove_apexes(x):
    x = x.replace("'", "")
    return x

# This function has to be applied to datasets which have square brackets encapsulating
# attribute values (string). E.G.: [1378129381293] and not 1378129381293
# It is used through the apply pandas function:
# dataset[Attribute] = dataset.apply(remove_sq_brackets) -> Remove apexes to all values of Attribute column


def remove_sq_brackets(x):
    x = x.replace("[", "")
    x = x.replace("]", "")
    return x


# has_location_infos(r"C:\dataset\2013_pakistan_eq_cities.csv")
