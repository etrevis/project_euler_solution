n=21

Matrix = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
	Matrix[i][0] = 1
	Matrix[0][i] = 1
for a in range(1,n):
	for b in range(1,n):
		Matrix[a][b] = Matrix[a-1][b]+Matrix[a][b-1]
print (Matrix[n-1][n-1])
