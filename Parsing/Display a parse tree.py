# Display a parse tree

# import treebank corpus
from nltk.corpus import treebank

    # Demo
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
