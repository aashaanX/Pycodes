#!/bin/python3

import sys

def getRecord(s):
	largest=s[0]
	smallest=s[0]
	largest_count = 0
	smallest_count = 0
	for i in s:
		if i>largest:
			largest_count+=1
			largest = i
		if i<smallest:
			smallest_count += 1
			smallest = i
	return largest_count,smallest_count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
largest_count,smallest_count = getRecord(s)
print(largest_count,smallest_count)