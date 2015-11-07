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
	data1[i]=string2stem([line.decode('utf-8').strip() for line in data[i].split()])

words = word2synonyms(word)
words1 = string2stem(words)
k=[]
kk=[]
for i in range(len(words1)):
	for j in range(len(data)):
		if words1[i] in data1[j]:
			if j not in kk:
				k.append(j)
				kk.append(j)
	if i == 0:
		if len(k)>0:
			print str(len(k)) + " results found."
			for ii in range(len(k)):
				print "Result #", str(ii+1), " - ",  "\"", data[k[ii]], ".\"\n"
			k = []
	else:
		if len(k)>0:
			print str(len(k)) + " results found replacing " + "\"" + words[0] + " with synonym " + words[i] + "\"."
			for ii in range(len(k)):
				print "Result #", str(ii+1), " - ", "\"", data[k[ii]], ".\"\n",
			k = []
