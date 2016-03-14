__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

# import models
from nltk.corpus import brown    # import brown corpus
from nltk import Text            # import text nltk model

# brown corpus words
brown_words = brown.words(categories='humor')
print(brown_words)

# generate text from brown words
brownText = Text(brown_words)
print(brownText)

print(brownText.collocations())

print(brownText.count("car"))

print(brownText.similar('humor'))
