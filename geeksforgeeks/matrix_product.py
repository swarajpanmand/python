import numpy as np

def product(mat):
    res = 1
    for i in mat:
        for j in i:
            res = res*j
    return res

A = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

B = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]


print(product(A))
print(product(B))