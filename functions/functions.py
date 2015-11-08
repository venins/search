"""
Module_name : functions
This module content some of commmon functions

-> findword: this function will return true if exact word is available in string.
-> file2string: This will take the file_name and return the file content as a string
-> word2synonyms: this will take word and return list with all synonyms of that word
-> string2stem: this will take the list of the stirngs and return stem list of strings
-> string2stem_word: stemmer for single word
"""

import re

from nltk.corpus import wordnet as wn
from nltk.stem.porter import *

#looking for word in sentence
def findword(word, string):
	"""find the whole word in the sentence using the regular experession"""
	data = re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search(string)
	if data == None:
		return False
	else:
		return True


#function to take filename and return string
def file2string(file_name):
	"""take the file name and return its content in the string"""
	file_content = open(file_name, 'r').read()
	return file_content

#function to find all common synonyms words
def word2synonyms(word):
	"""generate all synonyms of perticular word"""
	synonyms_words = []
	synonyms_words.append(word)
	for i,j in enumerate(wn.synsets(word)):
		name_list = j.lemma_names()
		for name in name_list:
			if name not in synonyms_words:
				synonyms_words.append(name)
	return synonyms_words

#function will take list of strings and stemm the all strigns inside the list
def string2stem(stringlist):
	"""convert the whole list items into stemm value and
	return the list of stemm"""
	stemmer = PorterStemmer()
	stemmstring = [stemmer.stem(string) for string in stringlist]
	return stemmstring

#function to take single word and return stem of word
def string2stem_word(word):
	"""take a single word and creturn stemm of word"""
	stemmer = PorterStemmer()
	return stemm.stem(word)

def file2list(file_name):
	"""convert the text file content into period
	seperated list."""
	file_content = file2string(file_name)
	file_content_list = file_content.split(".")
	return file_content_list