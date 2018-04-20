# Function that takes the tweet as input and returns:
# True: If the tweet has a geotag
# False: If not

# We need to check whether the place attribute is present in the tweet


def is_geotagged(tweet):
    return "place" in tweet
