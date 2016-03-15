#!/bin/python3

import sys

def cal_threshold(a):
	threashold = 0
	for i in a:
		if i<= 0:
			threashold +=1
	return threashold
ans=[]
t = int(input().strip())
for a0 in range(t):
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	a = [int(a_temp) for a_temp in input().strip().split(' ')]
	if k > cal_threshold(a):
		ans.append("YES")
	else:
		ans.append("NO")
for i in ans:
	print(i)

