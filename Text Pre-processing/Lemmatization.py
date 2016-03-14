__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'


# WordNetLemmatizer is using wordnet
from nltk.stem import WordNetLemmatizer

# create obj of the WordNetLemmatizer
word_lemma = WordNetLemmatizer()

# User Input
word = input("Please Enter Your Word: ")

# Word lemma -> the root word
root = word_lemma.lemmatize(word)

print (root)

