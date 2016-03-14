__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

sent = "Hi Everyone !  How do you do ?"

print("# Split() built-in string function")
print (sent.split())

#-----------------------------------------------------#

print("# word_tokenize")
from nltk.tokenize import word_tokenize
print (word_tokenize(sent))

#-----------------------------------------------------#

from nltk.tokenize import regexp_tokenize, wordpunct_tokenize,blankline_tokenize

print("# RegEx -> splite text by RegEx")
print(regexp_tokenize(sent, pattern='\w+'))

print("# wordpunct_tokenize : split text words")
print(wordpunct_tokenize(sent))

print("# blankline_tokenize : split text lines")
print(blankline_tokenize(sent))
