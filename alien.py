def subset(capacity, items):
	if capacity <= 0 or items == []:
		return 0
	elif items[0] > capacity:
		return subset(capacity, items[1:])
	else:
		loseIt = subset(capacity, items[1:])
		useIt = items[0] + subset(capacity - items[0], items[1:])
		return max(loseIt, useIt)
print (subset(10, [6,8,4]))
