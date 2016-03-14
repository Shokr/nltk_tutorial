__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

print("## String edit distance ##")

from nltk.metrics import *

s1 = input("Enter Text 1: ")
s2 = input("Enter Text 2: ")

print(edit_distance(s1, s2))
print("-----------------------------------")
