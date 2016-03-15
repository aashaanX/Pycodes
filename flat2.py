import time

def swapa(flat,element,e,temp,tempn):
	print('test')
	print(e)
	print(element)
	print(flat[element])
	if temp.count(temp[tempn]) !=1:
		tempn = temp.index(temp[tempn])
	else:
		pass
	if flat.count(None) == 1:
		status = False
		return flat
	elif element == e and flat[e] == flat[element]:
		status = False
		return flat
	elif flat[element] == None:
		print('here2')
		flat[flat[element]] = element
		flat[element] = tempn
		status = False
		return flat
	elif flat[flat[element]] != None:
		print('here3')
		print(temp[flat[element]-1])
		return swapa(flat,temp[flat[element]-1][1],e,temp,tempn)
			
n,m = input().strip().split(' ')
n=int(n)
m=int(m)
temp = []
for a0 in range(n):
	a,b = input().strip().split(' ')
	temp.append([int(a),int(b)])
flat=[]
for i in range(m+1):
	flat.append(None)
count = 0
print(temp)
for j in range(len(temp)):
	print(flat)
	if flat[temp[j][0]] == None:
		count +=1
		flat[temp[j][0]] = j+1
		continue
	elif flat[temp[j][1]] == None:
		count +=1
		flat[temp[j][1]] = j+1
	elif flat[temp[j][0]] != None and flat != swapa(flat,temp[j][0],temp[j][0],temp,j):
		print('here')
		count +=1
		flat = swapa(flat,temp[j][0],temp[j][0],temp,j)
	elif flat[temp[j][1]] != None and flat != swapa(flat,temp[j][1],temp[j][1],temp,j):
		print('here1')
		count +=1
		flat = swapa(flat,temp[j][1],temp[j][1],temp,j)
	else:
		pass

print(count)
print(flat)
