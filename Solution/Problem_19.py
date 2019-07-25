# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# 1st Jan 1901 is on Thursday
year_dict = {"N": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
             "L": [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]}  # N = Normal, L = Leap, U = Use
day = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}


def find_sunday():
    sunday = 0
    first_day = 2  # The First day of year 1901 is on Tuesday
    for year in range(1901, 2001):
        print ("\nYear", year)
        if year % 4 != 0:
            year_dict["U"] = year_dict["N"]
        else:
            year_dict["U"] = year_dict["L"]
        month = 1
        for number_of_days in year_dict["U"]:
            print ("First day of month %d is %s" % (month, day[first_day]))
            first_day = (first_day + number_of_days % 7) % 7
            # Take the first day and plus to the remain days. Then mod by 7 in case >7
            if first_day == 0:
                sunday += 1
            month += 1
        print ("Total number of Sundays up to this year is:", sunday)
    return sunday


find_sunday()
