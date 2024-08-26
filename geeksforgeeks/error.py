a = [2,3,5,6,7,9,1]

def sum():
    for i in range(7):
        for j in range(i+1, 7):
            if a[i] +  a[j] == 10:
                return i, j

print(sum())

                
