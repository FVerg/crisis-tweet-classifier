# Function which calculates the time in days the user (The one who posted
# the tweet with tweet id passed as parameter) has been on Twitter, since his
# first registration.

# Todo:
#   - Manage exceptions for non existing tweets
#   - Format the string (created_at) returned by twitter in order to fit in a datetime obj
#   - Create a datateime obj containing the new date
#   - Calculate and return elapsed time since the registration

months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def user_age(creation_date):
    import datetime as dt

    now = dt.datetime.now()

    words = []

    # Splitting the string to extract separately date and time
    # Structure: DayOfWeek Month Day Hour +0000 Year
    for word in creation_date.split(" "):
        words.append(word)

    # Extracting creation date and time of the account
    date = {"Year": words[len(words)-1], "Month": months[words[1]], "Day": words[2]}
    time = words[3].split(":")
    registration_date = dt.datetime(int(date["Year"]), int(date["Month"]),
                                    int(date["Day"]), int(time[0]), int(time[1]), int(time[2]))
    '''
    print("Now: ", now)
    print("Registration date: ", registration_date)
    '''
    # Extracting days from deltatime
    # Structure: xxxx Days, ...
    # This way str(now-registration_date).split(" ")[0]:
    #  - First splits the string using spaces as delimiter
    #  - Then returns the first element of the list

    elapsed_days = str(now-registration_date).split(" ")[0]

    return elapsed_days
