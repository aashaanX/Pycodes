#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
def primary(a):
	p_dig = 0
	for i in range(n):
		p_dig += a[i][i]
	return p_dig
def secondary(a):
	s_dig = 0
	for i in range(n):
		s_dig += a[i][n-1-i]
	return s_dig
print(abs(primary(a) - secondary(a)))
