#!/bin/python3

import sys


t = int(input().strip())
temp=[]
for a0 in range(t):
	n = int(input().strip())
	temp.append(n)

for i in temp:
	height = 1
	flag=0
	for x in range(i):
		if flag==0:
			height=height*2
			flag=1
		elif flag==1:
			height +=1
			flag=0
	print(height)
