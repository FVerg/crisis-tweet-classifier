# Function which calculates the time in days the user (The one who posted
# the tweet with tweet id passed as parameter) has been on Twitter, since his
# first registration.

# Todo:
#   - Manage exceptions for non existing tweets
#   - Format the string (created_at) returned by twitter in order to fit in a datetime obj
#   - Create a datateime obj containing the new date
#   - Calculate and return elapsed time since the registration


def user_age(id):
    import datetime as dt
    now = dt.datetime.now()
    tweet = twitter.show_status(id=id)
    registration_date_time = tweet['user']['created_at']
    print("Now: ", now)
    print("Registration date: ", registration_date_time)
