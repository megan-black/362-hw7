
def leap(year):
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        return str(year) + " is a leap year"
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return str(year) + " is a leap year"