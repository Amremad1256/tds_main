def filter_words_by_length(words, length):
    filtered_words = []
    for word in words:
        if len(word) > length:
            filtered_words.append(word)
    return filtered_words

word_list = ["apple", "banana", "orange", "grapefruit"]
filtered_list = filter_words_by_length(word_list, 5)
print("Words longer than 5 characters:", filtered_list)