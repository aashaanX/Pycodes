#!/bin/python3

import sys

i=0
def lis(n):
	i=0
	value=[]
	while i*i <= n:
		value.append(i*i)
		i+=1
	return value
t = int(input().strip())
temp=[]
for a0 in range(t):
	a,b =(input().split(" "))
	com=[int(a.strip()),int(b.strip())]
	temp.append(com)
large=0;
for x in temp:
	if large<=x[1]:
		large=x[1]
value=lis(large)
	
for x in temp:
	count=0
	for i in value:
		if i>=x[0] and i<=x[1]:
			count+=1
	print(count)
