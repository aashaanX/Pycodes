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

def check(new_grid,P):
	if new_grid == P:
		return True
	else:
		return False
for X in temp:
	for i in range(X[2]):
		for j in range(X[3]):
			
