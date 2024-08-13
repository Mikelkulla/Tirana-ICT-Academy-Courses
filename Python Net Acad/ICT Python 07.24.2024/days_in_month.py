"""
Lab 4.3.1.7
Ndertimi i nje funksioni qe merr dy parametra vitin dhe nr e muajt
dhe afishon ditet e atij muaji per ate vit. Duhet te shfrytezojme
edhe funksionin e shkraur te file: 4.3.1.6 Lab Leap Year

Shembuj:
2024 7 funksioni kthen 31
2024 2 funksioni kthen 29
2024 11 funskioni kthen 30
2024 0 funksioni kthen None
"""
# nga moduli Lab_Leap_Year kemi importuar funksionin leap_year
from is_leap_year import leap_year


def days_in_month(year: int, month: int) -> int or None:
    if month < 1 or month > 12:
        return None
    if leap_year(year) is None:
        return None
    month_30 = [4, 6, 9, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if month in month_30:
        return 30
    elif month in month_31:
        return 31
    elif leap_year(year):
        return 29
    else:
        return 28


def main():
    test_years = [1900, 2000, 2016, 1987, 2024, 2024, 2100, 2024, 2024, 2024, 2024]
    test_months = [2, 2, 1, 11, 7, 7, 2, 11, 12, 15, 0]
    test_results = [28, 29, 31, 30, 31, 31, 28, 30, 31, None, None]
    for i in range(len(test_years)):
        yr = test_years[i]
        mo = test_months[i]
        print(yr, mo, "->", end="")
        result = days_in_month(yr, mo)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")


# parandalon qe rezultatet te shfaqen tek filet qe e therasin kete file
if __name__ == '__main__':
    main()
