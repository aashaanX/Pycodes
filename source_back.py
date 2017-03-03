#!/bin/python3

import sys

number = int(input())

def sumOfNumbers(num,ans):
	if num  == 0:
		return ans
	ans = ans+int(num/10)
	return sumOfNumbers(int(num/10),ans)
#print(number+sumOfNumbers(number,0))

def reveSumNumber(num,constant_number):
    for i in range(num,0,-1):
        if(i+sumOfNumbers(i,0)==constant_number):
            return i
    return "failed"

print(reveSumNumber(number,number))



