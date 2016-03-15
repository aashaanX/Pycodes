def Increment(list_to):
	if list_to == []:
		return []
	else:
		list_to[0]=list_to[0]+1
		return [list_to[0]]+Increment(list_to[1:])


print(Increment([10,20,30]))


