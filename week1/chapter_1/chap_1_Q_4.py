import datetime
age = float(input("Enter Your age : "))
today = datetime.date.today()
year = today.year
print ("You were born in :" , year - age)