"""
Module_name : functions
This module content some of commmon functions

-> findword: this function will return true if exact word is available in string.
-> file2string: This will take the file_name and return the file content as a string
-> word2synonyms: this will take word and return list with all synonyms of that word
-> string2stem: this will take the list of the stirngs and return stem list of strings
-> string2stem_word: stemmer for single word
-> file2list: convert file into "." seperated sentences.
->wordwithsynonyms: the actule function which take filename and words and search the file
                    with words and its synonyms.
->all_files_in_dir: function to explore and add all file path in list.
"""
import os
import sys
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
	"""take the file name and return its content in the string."""
	file_content_old = open(file_name, 'r').read()
	#removed the special character "," as it join with the word and treated as diffrent word
	file_content_new = file_content_old.replace(",", "")
	return file_content_new

#function to find all common synonyms words
def word2synonyms(word):
	"""generate all synonyms of perticular word using nltk wordnet"""
	synonyms_words = []
	synonyms_words.append(word)
	for i,j in enumerate(wn.synsets(word)):
		#adding all layers of lemma_names in list
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
	#creating stemm of words using list comprehension
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
	#creating the list with sentences seperated by the dot
	file_content_list = file_content.split(".")
	return file_content_list

#real search funtion

def wordwithsynonyms(file_name, words):
	"""
	converting the users files contents into the
	list of sentences.
	"""
	file_content_list = None
	if file_name:
		file_content_list = file2list(file_name)

	"""
	using the list of sententces and storing its stemm form 
	using the string2stem function into new directory
	"""
	file_content_stemm_dict = {}
	for i in range(len(file_content_list)):
		file_content_stemm_dict[i] = string2stem([line.decode('utf-8').strip() for line in file_content_list[i].split()])

	"""
	creating loop for all user provided search words,
	it will iterate over one by one all words and 
	search for all possible words.
	"""

	for word in words:
		#Generating list of all synonyms of the word
		word_synonyms = word2synonyms(word)
		#converting all word synonyms in list formate
		word_synonyms_stemm = string2stem(word_synonyms)
		"""
		creating two list to store the found sententces index.
		one is to store unique index other to check number total
		for that perticular loop
		"""
		total_index = []
		local_index = []

		for i in range(len(word_synonyms_stemm)):
			for j in range(len(file_content_list)):
				if word_synonyms_stemm[i] in file_content_stemm_dict[j]:
					if j not in total_index:
						local_index.append(j)
						total_index.append(j)
			if i == 0:
				print "Search for the word " + word + "========>\n"
				if len(local_index)>0:
					print str(len(local_index)) + " results found.\n"
					for ii in range(len(local_index)):
						print "Result #", str(ii+1), " - ",  "\"", file_content_list[local_index[ii]], ".\"\n"
				local_index = []
			else:
				if len(local_index)>0:
					print str(len(local_index)) + " results found replacing " + "\"" + word_synonyms[0] + " with synonym " + word_synonyms[i] + "\"."
					for ii in range(len(local_index)):
						print "Result #", str(ii+1), " - ", "\"", file_content_list[local_index[ii]], ".\"\n",
					local_index = []


#dir explore function
files_in_dir = []
def all_files_in_dir(dir_name):
	"""Explore directory for all files and folders
	and return list of all text files using recursive function.
	"""
	current_dir_files = os.listdir(dir_name)
	for dir_files in current_dir_files:
		#this will create full path file or folder name
		current_file_name = dir_name + "/" + dir_files
		if os.path.isfile(current_file_name) and current_file_name.endswith(".txt"):
			if current_file_name not in files_in_dir:
				files_in_dir.append(current_file_name)
		elif os.path.isdir(current_file_name):
			all_files_in_dir(current_file_name)
	return files_in_dir


def cmd_argv():
	"""accepting arguments from cmd"""
	try:
		if sys.argv[1] == "-f" or sys.argv[1] == "-d":
			option = sys.argv[1]
		else:
			print "Please select \"-f\" for single text file or \"-d\" for Full directory search"
	except:
		print "Please select \"-f\" for single text file or \"-d\" for Full directory search"
		sys.exit()

	try:
		if sys.argv[2].endswith(".txt") and option == "-f":
			file_name = sys.argv[2]
		elif option =="-d":
			dir_name = sys.argv[2]
		else:
			print "please enter text file name or directory name with proper option"
	except:
		print "Please enter .txt file name"
		sys.exit()

	try:
		if len(sys.argv) > 3:
			for args in sys.argv[3:]:
				if args not in words:
					words.append(args)
		else:
			print "Please enter one or more words to search"
	except:
		print "Please enter one or more words to search"
		sys.exit()
