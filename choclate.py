#!/bin/python3

import sys
def AddedChoclate(wrapers,M):
	if wrapers//M == 0:
		return 0
	else:
		 return (wrapers//M)+AddedChoclate((wrapers-(wrapers//M)*M)+(wrapers//M),M)

#int(int(i[0]/i[1])/i[2])
t = int(input().strip())
temp = []
for a0 in range(t):
	n,c,m = input().strip().split(' ')
	n,c,m = [int(n),int(c),int(m)]
	temp.append([n,c,m])
for i in temp:
	initial_choclate = (i[0]//i[1])
	wrapers = initial_choclate
	print(initial_choclate+AddedChoclate(wrapers,i[2]))


