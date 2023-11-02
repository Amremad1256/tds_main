def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

sentence = input("Enter a sentence: ")
capitalized_sentence = capitalize_words(sentence)
print("Capitalized sentence:", capitalized_sentence)