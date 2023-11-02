import string

def read_text_file(Sample):
    with open(Sample, 'r') as file:
        text = file.read()
    return text

def split_into_words(text):
    words = text.split()
    return words

def get_unique_words(words):
    unique_words = set()
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word.isalpha():
            unique_words.add(word)
    return unique_words

def count_word_frequency(word, words):
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count

def print_word_frequencies(words):
    frequencies = {}
    for word in words:
        frequencies[word] = count_word_frequency(word, words)
    for word, frequency in frequencies.items():
        print(f"{word}: {frequency}")

def save_word_frequencies(file_name, words):
    frequencies = {}
    for word in words:
        frequencies[word] = count_word_frequency(word, words)
    with open(file_name, 'w') as file:
        for word, frequency in frequencies.items():
            file.write(f"{word}: {frequency}\n")

# Main program
file_name = "input.txt"
text = read_text_file(file_name)
words = split_into_words(text)
unique_words = get_unique_words(words)

print("Word frequencies:")
print_word_frequencies(unique_words)

output_file_name = "word_frequencies.txt"
save_word_frequencies(output_file_name, unique_words)
print(f"Word frequencies saved to {output_file_name}.")