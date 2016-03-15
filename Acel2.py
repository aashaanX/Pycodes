#!/bin/python3

import sys

def mthgreatest(s,m):
	l = list(s)
	l.sort()
	if min(l) != 1:
		return l[len(l)-m]
	else:
		return max(s) - m +1

def S1(s):
	s= list(s)
	for i in s:
		for j in s:
			if i!=j:
				s.append(abs(i-j))
				s=list(set(s))
	return set(s)




n = int(input().strip())
s=[int(x) for x in input().strip().split(' ')]
m = int(input().strip())
s= set(s)
while len(s) != len(S1(s)):
	s = S1(s)
	if min(s) == 1:
		break
print(mthgreatest(s,m))
