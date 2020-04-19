import nltk
from nltk.corpus import wordnet, brown
from nltk.text import ContextIndex

words = [word.lower() for word in brown.words()]
text = ContextIndex(words)

test_string = "Hello World"

# new_list_of_words = []

for w in nltk.word_tokenize(test_string):
    print(f"{w} => {text.similar_words(w)}")