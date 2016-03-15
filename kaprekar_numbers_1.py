def kaprekar(n):
	if n>3:
		number = n*n
		length = len(str(number))
		left = int(str(number)[0:length//2])
		right = int(str(number)[length//2:length])
		if left+right == n:
			return True
		else:
			return False

min_limit=int(input())
max_limit=int(input())
temp=[]
for i in list(range(min_limit,max_limit+1,1)):
	if kaprekar(i) or i==1:
		temp.append(i)
if len(temp)==0:
	print('INVALID RANGE')
else:
	ans=''
	for i in temp:
		ans=ans+str(i)+' '
	print(ans)
