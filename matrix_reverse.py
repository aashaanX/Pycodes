
def matrix_input(m,n):
	matrix=[]
	for i in range(m):
		temp=input().split(' ')
		matrix.append(temp)
	return matrix
m=int(input())
n=int(input())
matrix=(matrix_input(m,n))

def boundary(matrix):
	m=len(matrix)
	n=len(matrix[0])
	temp=[]
	for i in range(m):
		for j in range(n):
			if i==0 or j==0:
				temp.append(matrix[i][j])
			if i == m or j == n:
				temp.append(matrix[i][j])
	return temp
print(boundary(matrix))
