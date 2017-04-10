#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
s = list(map(int, input().strip().split(' ')))
b_charged = int(input().strip())
b_actual=0
for i in range(len(s)):
	if(i!=k):
		b_actual = b_actual+s[i]
if (b_actual//2)==b_charged:
	print("Bon Appetit")
else:
	print(b_charged-b_actual//2)