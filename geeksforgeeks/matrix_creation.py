n = int(input())

print("dimension of the matrix are: "+ str(n))
res= []
for i in range(n):
    row = []
    for j in range(n):
        row.append(1+ n*i+j)
    res.append(row)

print("the creation matrix of n*n is: "+ str(res))
