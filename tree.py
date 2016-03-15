
def createTree(n):
	n=input()
	if n=='':
		return ['']
	else:
		return []+createTree(n)
n=input()
print(createTree(n))
	
	
