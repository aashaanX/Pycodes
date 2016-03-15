#!/bin/python3

import sys


t = int(input().strip())
temp=[]
for a0 in range(t):
	n = int(input().strip())
	temp.append(n)
for x in temp:
	value = str(x)
	count=0
	for i in value:
		if int(i) != 0:
			if x%int(i) ==0:
				count+=1
	print(count)
		

