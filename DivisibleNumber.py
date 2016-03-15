import sys
import time
sys.setrecursionlimit(3000)

def digitLen(n):
	if n//10 == 0:
		return 1
	else:
		return 1+digitLen(n//10)

def sumOfDigits(n):
	if n//10 == 0:
		return n
	else:
		return n%10+sumOfDigits(n//10)

def productOfDigits(n):
	if n//10 == 0:
		return n
	else:
		return (n%10)*productOfDigits(n//10)

def Divisible(n):
	if productOfDigits(n)!=0 and sumOfDigits(n)>=productOfDigits(n):
		return True
	else:
		return False

n=int(input())
i=1
while not Divisible(n*i):
	i=i+1
	print(n*i)
	time.sleep(1)
print(digitLen(n*i))
