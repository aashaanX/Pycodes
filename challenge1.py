def beautifulIndex(lista,listb):
	a= sorted(lista)
	b= sorted(listb)
	beautiful_pair=[]
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				beautiful_pair.append((i,j))
	return beautiful_pair
def countSet(lis):
	counts = []
	sets=list(set(lis))
	for i in sets:
		counts.append((i,lis.count(i)))
	return counts
def largest(lis):
	largest = None
	value = 0
	for i in lis:
		if value < i[1]:
			value = i[1]
			largest = [i[0],i[1]]
	return largest
	

lista = [1,2,2]
listb = [1,2,3]
print(beautifulIndex(lista,listb))
print(countSet(lista))
print(countSet(listb))
print(largest(countSet(listb)))
