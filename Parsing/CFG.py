__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

# Generating sentences from context-free grammars

from nltk.parse.generate import generate, demo_grammar
from nltk import CFG

# An example grammar:
grammar = CFG.fromstring(demo_grammar)
print(grammar)

print("#---------------------------------------------------------------#")

# The first 10 generated sentences:
for sentence in generate(grammar, n=10):
    print(' '.join(sentence))

print("#---------------------------------------------------------------#")

