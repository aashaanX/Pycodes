#!/bin/python3

import sys


string = input()
order = []
for i in string:
	order.append(i)

for i in order:
	if i == 'N':
		if 'S' in order:
			order.remove('N')
			order.remove('S')
	if i == 'S':
		if 'N' in order:
			order.remove('N')
			order.remove('S')
	if i == 'E':
		if 'W' in order:
			order.remove('E')
			order.remove('W')
	if i == 'W':
		if 'E' in order:
			order.remove('E')
			order.remove('W')

order.sort()
ans = ''
for i in order:
	ans = ans + i

print(ans)
