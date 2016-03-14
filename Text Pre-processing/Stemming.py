__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

# import Porter stemmer
from nltk.stem import PorterStemmer
# import Porter LancasterStemmer
from nltk.stem.lancaster import LancasterStemmer


# create obj of the PorterStemmer
pst = PorterStemmer()

# create obj of LancasterStemmer
lst = LancasterStemmer()


# LancasterStemmer
print(lst.stem("eating"))      #eat

# PorterStemmer
print(pst.stem("printed"))    #print
