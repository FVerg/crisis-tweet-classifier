import pandas as pd

dataset = pd.read_csv('C:/dataset/2013_pakistan_eq_metadata.csv', header=0)

deltatimes = dataset["DeltaTime"]
DeltaSec = []
for i, time in zip(range(0, len(deltatimes)), deltatimes):
    deltahours = time.split(":")[0]
    deltaminutes = time.split(":")[1]
    deltaseconds = time.split(":")[2]

    DeltaSec.append(int(deltahours)*360 + int(deltaminutes)*60 + int(deltaseconds))

del dataset["DeltaTime"]
dataset["DeltaSeconds"] = pd.Series(DeltaSec).values
print(dataset)

dataset.set_index('TweetID')
col_names = list(dataset.columns.values)
dataset.to_csv(r'metatweets.csv', header=col_names, index=False, sep=',', mode='w')
