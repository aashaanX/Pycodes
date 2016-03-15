
s=input()

def notcross(pal1,pal2):
	if pal1[1]<pal2[1]<pal1[2]:
		return False
	else:
		return True

def sort(lis):
	for i in lis:
		for j in lis:
			if i[3]<j[3]:
				temp = j
				j = i
				j = temp
	return lis

def palindrome(string):
	if string == string[::-1]:
		return True

palindrome_list = []
for i in range(len(s)+1):
	j=i+1
	while j<len(s):
		if palindrome(s[i:j]):
			palindrome_list.append([s[i:j],i,j,len(s[i:j])])
		j+=1
#palindrome_list = list(set(palindrome_list))
print(palindrome_list) 

def ans(palindrome_list):
	pal1=max(palindrome_list,key = lambda x: x[2])
	palindrome_list.remove(pal1)
	pal2=max(palindrome_list,key = lambda x: x[2])
	if palindrome_list == []:
		return None
	elif notcross(pal1,pal2):
		return pal1[3]*pal2[3]
	else:
		palindrome_list.remove(pal2)
		palindrome_list.append(pal1)
		ans(palindrome_list)

print(ans(palindrome_list))
