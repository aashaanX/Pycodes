#!/bin/python3

import sys


string = input()

for i in string:
	try:
		if i=='N':
			if 'S' in string:
				string =  string[0:string.index('N')]+string[string.index('N')+1:string.index('S')]+string[string.index('S')+1:]
		if i=='E':
			if 'W' in string:
				string =  string[0:string.index('E')]+string[string.index('E')+1:string.index('W')]+string[string.index('W')+1:]
		#if i=='S':
		#	if 'N' in string:
		#		string =  string[0:string.index('S')]+string[string.index('S')+1:string.index('N')]+string[string.index('N')+1:]
		#if i=='W':
		#	if 'E' in string:
		#		string =  string[0:string.index('W')]+string[string.index('W')+1:string.index('E')]+string[string.index('E')+1:]
	except ValueError:
		pass
print(string)

