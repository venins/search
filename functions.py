"""
Module_name : functions
This module content some of commmon functions
"""

import re

#looking for word in sentence
def findword(w,w1):
	data = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search(w1)
	if data == None:
		return False
	else:
		return True
