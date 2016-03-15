#!/bin/python3

import sys
di_con = {'12':'00','1':'13','2':'14','3':'15','4':'16','5':'17','6':'18','7':'19','8':'20','9':'21','10':'22','11':'23'}
time = input().strip()
hr= time.split(':')[0]
mi = time.split(':')[1]
sec = time.split(':')[2]
if 'AM' in sec:
	if hr=='12':
		hr=di_con[hr]
	sec=sec.strip('AM')
	print(hr+':'+mi+':'+sec)
if 'PM' in sec:
	if hr!='12':
		hr=di_con[hr]
	print(hr+':'+mi+':'+sec)
	

