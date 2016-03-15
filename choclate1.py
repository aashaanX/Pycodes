#N = Dollar he has 10
#C = Amount for a Choclate 2
#M = Offer for Wraper 4

N = 12
C = 4
M = 4
initial_choclate = (N//C)
wrapers = initial_choclate
def AddedChoclate(wrapers,M):
	if wrapers//M == 0:
		return 0
	else:
		 return (wrapers//M)+AddedChoclate((wrapers-(wrapers//M)*M)+(wrapers//M),M)

print(initial_choclate+AddedChoclate(wrapers,M))
