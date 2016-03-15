__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

import nltk

sent = "Mark is studying at Stanford University in California"
# Tokens
tokens = nltk.word_tokenize(sent)
# Tagged
tagged = nltk.pos_tag(tokens)
# Named Entity Extraction: ne_chunk.
entities = nltk.chunk.ne_chunk(tagged)

# Output
print(entities)
