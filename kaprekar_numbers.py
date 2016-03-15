def kaprekar(n):
	if left+right==n:
		return True
	elif right==None:
		return False
	else:
		left = int(str(left)+str(right)[0])
		right = int(str(right)[1:])
		return left,right

print(kaprekar(45))
	
