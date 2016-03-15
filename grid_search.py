#!/bin/python3

import sys


t = int(input().strip())
temp=[]
for a0 in range(t):
	R,C = input().strip().split(' ')
	R,C = [int(R),int(C)]
	G = []
	G_i = 0
	for G_i in range(R):
		G_t = str(input().strip())
		G.append(G_t)
	r,c = input().strip().split(' ')
	r,c = [int(r),int(c)]
	P = []
	P_i = 0
	for P_i in range(r):
		P_t = str(input().strip())
		P.append(P_t)
	temp.append([G,P,R,C,r,c])
def start_index(G,P,R,C,r,c):
	starting_index = -1
	count = 0
	for j in P:
		for i in G:
			count +=1
			if j in i:
				for x in range(C):
					if i[x:x+c] == j:
						starting_index = x
						break						
			if starting_index !=-1:
				break
		if starting_index !=-1:
				break
	return count-1,starting_index
def check(X):
	row,column=start_index(X[0],X[1],X[2],X[3],X[4],X[5])
	new_grid=[]
	for i in range(row,row+X[4],1):
			new_grid.append(X[0][i][column:column+X[5]])
	print(new_grid)
	print(X[1])
	if X[1]==new_grid:
		return True,row
	else:
		return False,row
#print(start_index(G,P,R,C,r,c))
for X in temp:
	status,value=check(X)
	print(status,value,len(X[0]),X[4])
	while not status and len(X[0]) > X[4]:
			X[0]=X[0][value+1:]
			status,value=check(X)
			#print(value,X[2]-X[4])
	if status:
		print('YES')
	else:
		print('NO')
	
