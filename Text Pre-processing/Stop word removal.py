__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'
# Stop word removal is one of the most commonly used preprocessing steps across
# different NLP applications. The idea is simply removing the words that occur
# commonly across all the documents in the corpus.

#import stopwords Corpora
from nltk.corpus import stopwords

# NLTK supports 22 languages for removing the stop words
# config the language name
stoplist = stopwords.words('english')

# Input
text = "This is just a test"

cleanwordlist = [word for word in text.split() if word not in stoplist]

print(cleanwordlist)
