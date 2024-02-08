n= 3
res= []
for i in range(n):
    row=[]
    for j in range(n):
        row.append(1 + n*i+j)
    res.append(row)
print(res)

k=2
print(res[2])
res2= [row[k] for row in res]
print(res2)