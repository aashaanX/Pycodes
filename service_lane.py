#!/bin/python3

import sys


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
temp=[]
for a0 in range(t):
	i,j = input().strip().split(' ')
	i,j = [int(i),int(j)]
	temp.append([i,j])
for i in temp:
	small = 4
	for j in range(i[0],i[1]+1,1):
		if width[j]<=small:
			small = width[j]
	
	print(small)	

