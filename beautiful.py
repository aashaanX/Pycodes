s = input()
temp=[]
for i in range(len(s)):
	j=i+1
	while j!=len(s):
		temp.append(s[0:i]+s[i+1:j]+s[j+1:])
		j+=1
temp=set(temp)
print(len(temp))

