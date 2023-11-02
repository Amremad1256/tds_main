sentence = input("Enter the sentence you want to revers :")

def reverse_words (sentence):
    word = sentence.split(' ') 
    reverse_sentence = ' '.join(reversed(word)) 
    return reverse_sentence


reversed_sentence = reverse_words(sentence)
print("Reversed sentence:", reversed_sentence)
