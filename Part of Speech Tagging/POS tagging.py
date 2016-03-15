__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

print("##Part of Speech Tagging##")

import nltk
from nltk import word_tokenize

s ="""
this is a demo that will show you how to detects parts
of speech with little effort using NLTK!
"""

print(nltk.pos_tag(word_tokenize(s)))

