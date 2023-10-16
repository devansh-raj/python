print("DEVANSH")
print("24. Python program to implement matrix multiplication: ")
X = [[3,5,1],
[1 ,3,2],
[4 ,6,3]]
Y = [[4,5,3],
[2,5,7],
[2,4,1]]
result = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for x in result:
    print(x)
