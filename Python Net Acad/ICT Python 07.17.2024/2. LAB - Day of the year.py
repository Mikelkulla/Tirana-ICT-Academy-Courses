

def is_year_leap(year):
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return False

def days_in_month(year, month):
    leap = is_year_leap(year)
    daysinmonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if leap:
        daysinmonth[2] = 29
    else:
        daysinmonth[2] = 28
    return daysinmonth[month]


def day_of_year(year, month, day):
    days_in_previous_months = 0
    if year < 1 or month<1 or month >12 or day < 1:
        return None
    if day > days_in_month(year,month):
        return None
    else:
        for i in range(month):
            days_in_previous_months += days_in_month(year, i)
    return days_in_previous_months + day

print(day_of_year(1924, 7, 24))
