__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

"""
Relation Extraction

In the following code,
a relationship between an organization and a location has been defined and
we want to extract all the combinations of these patterns.
""" 

import nltk
import re
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer',pattern = IN):
        print(nltk.sem.rtuple(rel))
