"""
module name: search
descriptions: This will use to main module to search the word and word's synonyms from text files.
"""
import sys

from functions import *

script_name, option, file_name, word = sys.argv

data = file2string(file_name)
data = data.split(".")
data1 = {}
for i in range(len(data)):
	data1[i]=string2stem(data[i].split())

words = word2synonyms(word)
#print words
words1 = string2stem(words)
k=[]
for i in range(len(words1)):
	for j in range(len(data)):
		if words1[i] in data1[j]:
			if j not in k:
				k.append(j)

for i in k:
	print data[i]
