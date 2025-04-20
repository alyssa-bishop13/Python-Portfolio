#april 15th 2025
#Source: Calculate Remaining Time Until a Birthday with Python. Codevisionz. https://codevisionz.com/lessons/python-calculation-of-remaining-time-until-birthday/
#how many days until birthday?
import datetime

month = int(input("Enter birth month(1-12): "))
day = int(input("Enter birth day(1-31): "))

today = datetime.date.today()
year = today.year

birthday = datetime.date(year, month, day)
if birthday < today:
    birthday = datetime.date(year + 1, month, day)

days_left = (birthday - today).days
print(f"Your birthday is in {days_left} days!")