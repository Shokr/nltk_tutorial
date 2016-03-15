__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

# WordNet
from nltk.corpus import wordnet as wn

# User Input
#word = input("Enter Word: ")
word = "gone"

# The root
root = wn.morphy(word)

print("The Result: ")
print(root)
