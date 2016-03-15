def fib(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	elif n==3:
		return 2
	else:
		return fib(n)+fib(n-1)

n=int(input("enter the number"))
print(fib(n))
