from functions import *

data = file2string("test.txt")
data = data.split(".")
print data
data1 = {}
for i in range(len(data)):
	data1[i]=string2stem([line.decode('utf-8').strip() for line in data[i].split()])