s= input()

def palindrome(a):
	if a == a[::-1]:
		return True
def makeList(s):
	pal_list = []
	for i in range(len(s)+1):
		for j in range(len(s)+1):
			if palindrome(s[i:j]):
				pal_list.append([s[i:j],i,j,len(s[i:j])])
	return list(filter(lambda x: x[0]!='',pal_list))

final = list(reversed(sorted(makeList(s),key =  lambda x: x[3])))

#print(final)

def ans(s):
	final = list(reversed(sorted(makeList(s),key =  lambda x: x[3])))
	biggest = 0
	for i in final:
		for j in final[1:]:
			if i[1]<i[2]<j[1] and j[2]<i[1]<i[2]:
				if biggest < i[3]*j[3]:
					biggest = i[3]*j[3]
	return biggest

print(ans(s))
