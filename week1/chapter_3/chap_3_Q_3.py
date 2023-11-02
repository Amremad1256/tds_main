from collections import Counter
import re

def count_words(text):
    words = re.findall(r"\w+", text.lower())
    word_counts = Counter(words)
    return dict(word_counts)

text = "This is a test. This is only a test."
word_counts = count_words(text)
print("Word frequencies:", word_counts)