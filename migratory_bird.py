#!/bin/python3

import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
counter=[0,0,0,0,0,0]
for i in types:
	counter[i]=counter[i]+1
	
print(counter.index(max(counter)))