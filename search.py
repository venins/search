import sys

from functions.functions import *

def main():
	words = []
	option = None
	file_name = None
	dir_name = None

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

	if option == "-f":
		wordwithsynonyms(file_name, words)
	elif option == "-d":
		files_in_dir = []
		files_in_dir = all_files_in_dir(dir_name)
		for files in files_in_dir:
			print "Searching in file " + files + "\n"
			wordwithsynonyms(files, words)


if __name__ == "__main__":
	main()