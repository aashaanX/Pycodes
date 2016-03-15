#!/bin/python3

import sys

def decent_num(n):
	decent= False
	for i in range(100000):
		for j in range(100000):
			if ((3*j)+(5*i))==n:
				decent=True
	return decent

def replace(queue):
	queue = queue[5:]
	for i in range(5):
		queue.append(3)
	return queue

def descent(queue,n):
	num_5 = 0
	num_3 = 0
	for i in queue:
		if i == 5:
			num_5 +=1
		else:
			num_3 +=1
	if num_5%3 ==0 and num_3%5 == 0 and len(queue)==n:
		return True
	else:
		return False	
temp=[]
t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	temp.append(n)
for x in temp:
	queue = []
	for i in range(x):
		queue.append(5)
	while not descent(queue,x):
		if not descent(queue,x) and 5 in queue:
			queue=replace(queue)
		if not descent(queue,x) and 5 not in queue:
			queue=[]
			break
	string = ''
	for i in queue:
		string+=str(i)
	if len(string) == 0:
		print(-1)
	else:
		print(int(string))

