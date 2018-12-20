#!/bin/python3
import os
import sys
import glob
#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#filename = dname + sys.argv[1]
path = '*.txt'
files = glob.glob(path)
for file in files:
	#arr = open(filename).readlines()
	arr = open(file).readlines()
	for lst in arr:
		mylist = lst[:5]
		mylist2 = lst[8:13]
		if mylist.strip() != mylist2.strip():
			#print("matched")
		#else:
			print(file +" - "+ mylist +" - "+ mylist2 +" = notmatched")
