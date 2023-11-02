minutes = int(input("Enter the number of minutes: "))

hours = minutes // 60  
remaining_minutes = minutes % 60  


print(f"{minutes} minutes are equal to {hours} hour(s) and {remaining_minutes} minute(s)")