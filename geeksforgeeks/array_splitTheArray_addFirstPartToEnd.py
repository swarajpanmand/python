arr = [12, 10, 5, 6, 52, 36]
n= len(arr)
x = arr[:2]
y = arr[2:]
y.extend(x)
print(y)
