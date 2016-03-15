# Python 3 program to read an integer from STDIN and output it to STDOUT

# Read the variable from STDIN
n,m = input().strip().split(' ')
n=int(n)
m=int(m)
temp = []
for a0 in range(n):
	a,b = input().strip().split(' ')
	temp.append([int(a),int(b)])
flat=[]
for i in range(m+1):
	flat.append(0)
count = 0
for j in temp:
	if flat[j[0]-1] == 0:
		count +=1
		flat[j[0]-1] = 1
		continue
	elif flat[j[1]-1] == 0:
		count +=1
		flat[j[1]-1] = 1
	else:
		pass	

# Output the variable to STDOUT
print(count)

