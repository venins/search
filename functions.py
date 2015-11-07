"""
Module_name : functions
This module content some of commmon functions

-> findword: this function will return true if exact word is available in string.
-> file2string: This will take the file_name and return the file content as a string

"""

import re

#looking for word in sentence
def findword(word, string):
	data = re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search(string)
	if data == None:
		return False
	else:
		return True


#function to take filename and return string
def file2string(file_name):
	file_content = open(file_name, 'r').read()
	return file_content
