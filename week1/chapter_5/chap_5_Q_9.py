def get_unique_words(sentence):
    words = sentence.split()
    return list(set(words))

sentence = input("Enter a sentence: ")
unique_words = get_unique_words(sentence)
print("Unique words:", unique_words)