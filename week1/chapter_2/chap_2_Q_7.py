age = int(input("Enter your age: "))
citizenship_status = input("Enter your citizenship status: ")
def check_voter_eligibility(age, citizenship_status):
    if age >= 18 and citizenship_status == "citizen":
        return "You are eligible to vote in national elections."
    elif age >= 16 and citizenship_status != "citizen":
        return "You are eligible to vote in local elections but not in national elections."
    else:
        return "You are not eligible to vote."

result = check_voter_eligibility(age, citizenship_status)
print(result)