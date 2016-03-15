#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()
while len(arr) != 0:
	print(len(arr))
	val =arr[0]
	for i in range(len(arr)):
		arr[i] = arr[i]-val
	for i in arr:
		if i==0:
			arr=arr[1:]
	
	
