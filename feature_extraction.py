import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


dataset = pd.read_csv('C:/dataset/2014_california_eq_metadata.csv', header=0)

dataset = dataset.set_index("TweetID")

# There are some duplicates, we delete them using this line of code
dataset = dataset[~dataset.index.duplicated(keep='first')]

# Mapping boolean values of Geotagged column in 0,1

for ID in dataset.index:
    if (dataset.loc[ID, "Geotagged"]) == True:
        dataset.loc[ID, "Geotagged"] = 1
    else:
        dataset.loc[ID, "Geotagged"] = 0

# Mapping boolean values of Class Label column in 0,1

for ID in dataset.index:
    if dataset.loc[ID, "Label"] in ("caution_and_advice", "displaced_people_and_evacuations",
                                    "infrastructure_and_utilities_damage", "injured_or_dead_people",
                                    "missing_trapped_or_found_people", "other_useful_information"):
        dataset.loc[ID, "Label"] = 1
    else:
        dataset.loc[ID, "Label"] = 0

# Mapping boolean values of Verified column in 0,1

for ID in dataset.index:
    if (dataset.loc[ID, "Verified"]) == True:
        dataset.loc[ID, "Verified"] = 1
    else:
        dataset.loc[ID, "Verified"] = 0


del dataset["CreationTime"], dataset["Username"]
# print(dataset)

# Making everything up for sklearn usage

ds_array = dataset.values
ds_target = dataset["Label"].values

ds_array = ds_array.astype(int)

# Select the best features for classification
chi2_selector = SelectKBest(chi2, k=4)
kbest = chi2_selector.fit_transform(ds_array, ds_target)

print(kbest)
# print(dataset.index)
