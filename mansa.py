#!/bin/python3

import sys

temp=[]
t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	a = int(input().strip())
	b = int(input().strip())
	temp.append([n,a,b])


def func(n,a,b):
	i=0
	temp=[]
	while n>=0:
		ans = a*n+b*i
		i+=1
		n-=1
		temp.append(ans)
	return sorted(set(temp))

for i in temp:
	ans=(func((i[0]-1),i[1],i[2]))
	string=''
	for i in ans:
		string =string+str(i)+' '
	print(string) 	
