def is_palindrome(string):
    reversed_string = string[::-1]
    return string.lower() == reversed_string.lower()

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")