
# Find similar terms (word definitions) using Wordnet

from nltk.corpus import wordnet as wn
synsets = wn.synsets('wing')
print ([str(syns.part_holonyms() ) for syns in synsets])
