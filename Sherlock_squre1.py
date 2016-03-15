#!/bin/python3

import sys
import math


t = int(input().strip())
temp=[]
for a0 in range(t):
	a,b =(input().split(" "))
	com=[int(a.strip()),int(b.strip())]
	temp.append(com)
for x in temp:
	i=0
	value=[]
	count = 0
	for j in range(x[0],x[1]+1,1):
		if int(math.sqrt(j))*int(math.sqrt(j)) == j:
			count+=1
	print(count)
