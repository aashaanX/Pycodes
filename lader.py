#!/bin/python3

import sys
n = int(input().strip())
stri=""
for i in range(n):
	for j in range(n):
		stri +=" "
	stri +="#"
	print(stri.strip(" "))
