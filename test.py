from sys import argv
import re
from nltk.stem.porter import *
from nltk.corpus import wordnet as wn

"""
script, option, file_name, search_word = argv

def findword(w):
	return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

if option == "-f":
	file_content = open(file_name, 'r').read()
	file_sentence = file_content.split(".")
	for sentence in file_sentence:
		if findword(search_word)(sentence) != None:
			print sentence

script, option, file_name = argv
stemmer = PorterStemmer()
if option == "-f":
	file_content = open(file_name, 'r').read()
	file_sentence = file_content.split(".")
	for sentence in file_sentence:
		sentence = sentence.split(" ")
		single_sentence = [stemmer.stem(sentenc) for sentenc in sentence]
		print single_sentence


for i,j in enumerate(wn.synsets('custom')):
    print "Synonyms:", ", ".join(j.lemma_names())

t = []
for i,j in enumerate(wn.synsets('custom')):
    name = j.lemma_names()
    for each_name in name:
    	if each_name not in t:
    		t.append(each_name)

print t
"""

for i,j in enumerate(wn.synsets('life')):
    print "Synonyms:", i ,", ".join(j.lemma_names())
