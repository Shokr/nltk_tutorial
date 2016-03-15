__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

"""
Chunking

- code snippets to do some basic chunking
"""

# import models
import nltk
from nltk.chunk.regexp import *

# Sentence
test_sent="""
The prime minister announced he had asked the chief
government whip, Philip Ruddock, to call a special party room meeting for
9am on Monday to consider the spill motion."""

# Tokens
test_sent_tokens = nltk.word_tokenize(test_sent)

# POS Tagging
test_sent_pos = nltk.pos_tag(test_sent_tokens)

# Verb phrase sentence parser
rule_vp = ChunkRule(r'(<VB.*>)?(<VB.*>)+(<PRP>)?', 'Chunk VPs')
parser_vp = RegexpChunkParser([rule_vp],chunk_label='VP')

print (parser_vp.parse(test_sent_pos))

# Noun phrase sentence parser
rule_np = ChunkRule(r'(<DT>?<RB>?)?<JJ|CD>*(<JJ|CD><,>)*(<NN.*>)+','Chunk NPs')
parser_np = RegexpChunkParser([rule_np],chunk_label="NP")

print (parser_np.parse(test_sent_pos))
