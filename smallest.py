a = int(input().strip()) 
b = int(input().strip())
c = int(input().strip())

if (a>b):
	if (a>c):
		print(a)
	else:
		print(c)
if (b>c):
	if (b>a):
		print(b)
	else:
		print(a)
