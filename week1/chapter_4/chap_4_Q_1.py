def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count

text = "This is a test. This is only a test."
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)