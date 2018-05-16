import pandas as pd

dataset = pd.read_csv("C:/dataset/2013_pakistan_eq_temp.csv", header=0)

relevant_labels = ("caution_and_advice", "displaced_people_and_evacuations", "infrastructure_and_utilities_damage",
                   "injured_or_dead_people", "missing_trapped_or_found_people", "other_useful_information")

dataset = dataset[~dataset["Label"].isin(relevant_labels)]

dataset = dataset.set_index("TweetID")

col_names = list(dataset.columns.values)

dataset.to_csv("C:/dataset/2013_pakistan_eq_irrelevant.csv",
               header=col_names, index=True, sep=',', mode='w')
