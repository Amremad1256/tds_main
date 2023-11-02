def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

string = input("Enter a string: ")
string_without_vowels = remove_vowels(string)
print("String without vowels:", string_without_vowels)