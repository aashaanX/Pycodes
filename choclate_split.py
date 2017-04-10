#!/bin/python3

import sys

def getWays(squares, d, m):
	count = 0
	for i in range(len(squares)):
		sum=0
		for j in range(m):
			try:
				sum=sum+squares[i+j]
			except:
				sum=0
		if(sum==d):
			count+=1
	return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)
