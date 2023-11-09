# Q1. Function to calculate a person's age based on birthdate and current date.


from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1
    return age

# Q2. Function to calculate the number of days between two given dates.
from datetime import date

def calculate_date_difference(date1, date2):
    difference = abs(date2 - date1)
    return difference.days

# Q3. Function to find the weekday of a given date.
from datetime import date

def find_weekday(date):
    weekday = date.strftime("%A")
    return weekday

# Q4. Function to check if a given year is a leap year.
import calendar

def is_leap_year(year):
    return calendar.isleap(year)

# Q5. Function to format a date into a user-friendly string.
from datetime import date

def format_date(date):
    formatted_date = date.strftime("%B %d, %Y")
    return formatted_date



birthdate = date(1990, 5, 15)
age = calculate_age(birthdate)
print(age)  # Output: The person's age based on current date

date1 = date(2023, 1, 1)
date2 = date(2023, 1, 15)
difference = calculate_date_difference(date1, date2)
print(difference)  # Output: The number of days between the two dates

weekday = find_weekday(date(2023, 1, 15))
print(weekday)  # Output: The weekday of the given date

is_leap = is_leap_year(2024)
print(is_leap)  # Output: True if the year is a leap year, False otherwise

formatted_date = format_date(date(2023, 1, 15))
print(formatted_date)  # Output: The formatted date string