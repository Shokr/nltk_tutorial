__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

# WordNet
import nltk
from nltk.corpus import wordnet as wn

# Input
word = "gone"

# The root
root = wn.morphy(word)

print("The Result: ")
print(root)
