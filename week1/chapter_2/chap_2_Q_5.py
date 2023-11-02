# Input the month
month = input("Enter a month: ")


month = month.lower()


if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Autumn"
else:
    season = "Invalid month"

# Print the result
print(f"This month is in {month.capitalize()} is {season}.")