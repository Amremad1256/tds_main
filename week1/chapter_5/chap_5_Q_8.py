def replace_word(string, old_word, new_word):
    return string.replace(old_word, new_word)

string = input("Enter a string: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
new_string = replace_word(string, old_word, new_word)
print("New string:", new_string)