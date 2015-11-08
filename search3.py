import os

from functions import *

files_in_dir = []
def all_files_in_dir(dir_name):
	"""Explore directory for all files and folders
	and return list of all text files.
	"""
	current_dir_files = os.listdir(dir_name)
	for dir_files in current_dir_files:
		current_file_name = dir_name + "/" + dir_files
		if os.path.isfile(current_file_name) and current_file_name.endswith(".txt"):
			if current_file_name not in files_in_dir:
				files_in_dir.append(current_file_name)
		elif os.path.isdir(current_file_name):
			all_files_in_dir(current_file_name)
	return files_in_dir


files = all_files_in_dir("test")

for file in files:
	print file2string(file)