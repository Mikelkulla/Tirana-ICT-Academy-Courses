"""
Lab 4.3.1.8
Llogarit e sajta dite e vitit eshte
"""

from days_in_month import days_in_month
from is_leap_year import leap_year
def day_of_year(year, month, day):
    if day < 1 or days_in_month(year, month) == 31 and day > 31:
        print("Dita eshte me e madhe se 31 qe ka month!")
        return None
    if leap_year(year) is None:
        return None
    if days_in_month(year, month) is None:
        return None
    if days_in_month(year, month) == 30 and day > 30:
        print("Dita eshte me e madhe se 30 qe ka month!")
        return None
    if days_in_month(year, month) == 28 and day > 28:
        print("Dita eshte me e madhe se 28 qe ka month!")
        return None
    if days_in_month(year, month) == 29 and day > 29:
        print("Dita eshte me e madhe se 29 qe ka month!")
        return None
    day_of_the_year = 0
    for m in range(1, month):
        day_of_the_year += days_in_month(year,m)
    day_of_the_year += day
    return day_of_the_year

def main():
    print(day_of_year(2024, 7, 24))
    print(day_of_year(2024, 2, 29))
    print(day_of_year(2025, 2, 36))

if __name__ == '__main__': main()
