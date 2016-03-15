#!/bin/python3

import sys
import math

s = input().strip()

length = len(s)
s_root = math.sqrt(length)
if s_root == int(s_root):
	row = int(s_root)
	column = int(s_root)
else:
	row = int(s_root)
	column = row+1
	if row*column < length:
		row = row+1
temp=[]
for i in range(row):
	temp.append(s[0:column])
	s=s[column:]
ans=''
for i in range(column):
	for j in temp:
		try:
			ans=ans+(j[i])
		except IndexError:
			pass
	ans=ans+' '
print(ans)
	

	
