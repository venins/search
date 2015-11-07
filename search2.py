"""
module name: search2
description: this module will support multiples words at once
"""

import sys

from functions import *

words = []
option = None
file_name = None

#accepting arguments from the cmd
try:
	if sys.argv[1] == "-f" or sys.argv[1] == "-d":
		option = sys.argv[1]
	else:
		print "Please select \"-f\" for single text file or \"-d\" for Full directory search"
except:
	print "Please select \"-f\" for single text file or \"-d\" for Full directory search"
	sys.exit()

try:
	if sys.argv[2].endswith(".txt"):
		file_name = sys.argv[2]
	else:
		print "Please only enter .txt files"
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
