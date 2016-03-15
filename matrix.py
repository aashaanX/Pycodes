#!/bin/python3

import sys


n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
	grid_t = str(input().strip())
	grid.append(grid_t)
if n!=1:
	print(grid[0])
for i in range(1,n-1):
	temp = grid[i]
	for j in range(1,n-1):
		if grid[i][j] > grid[i][j-1] and grid[i][j]> grid[i][j+1] and grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j]:
			temp = temp[0:j]+'X'+temp[j+1:]
	print(temp)
print(grid[n-1])
