import datetime as dt

months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def str_to_datetime(str_time):
    date_and_time = []
    # Splitting the string to extract separately date and time
    # Structure: DayOfWeek Month Day Hour +0000 Year
    for word in str_time.split(" "):
        date_and_time.append(word)

    # Extracting creation date and time
    date = {"Year": date_and_time[len(date_and_time)-1],
            "Month": months[date_and_time[1]], "Day": date_and_time[2]}
    time = date_and_time[3].split(":")
    out_date = dt.datetime(int(date["Year"]), int(date["Month"]),
                           int(date["Day"]), int(time[0]), int(time[1]), int(time[2]))

    return out_date
