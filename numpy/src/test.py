import numpy as np

arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(np.__version__)
print(type(arr))


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(arr2)

print(arr[1])
print(c[0, 2])
print(c[1][2])

print(d[0, 1, 2])
print(d[1][1][0])

print(c[1,-1])
print(c[1][-1])


# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
print(arr[1:3])
print(arr[1:])
print(arr[:3])   # from the start to index 3 (not included)
print(arr[-3:-1]) # negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(arr[1:5:4]) # return every other element from index 1 to index 5
print(arr[::2]) # return every other element from the entire array

print(c[1, 1:7])
print(c[0:2,2])   # from both elements return index 2
print(c[0:2, 0:2]) # from both elements return index 0 and 1


print(arr.dtype)
arr3 = np.array(['apple', 'banana', 'cherry'])
print(arr3.dtype)
arr4 = np.array([1, 2, 3, 4], dtype='S')
print(arr4.dtype)

arr5 = np.array([1, 2, 3, 4], dtype='i4')
print(arr5)

arr6 = np.array([1.1, 2.1, 3.1])
newarr = arr6.astype('i')
print(newarr)
newbool = newarr.astype(bool)
print(newbool)


x = arr.copy()
y = arr.view()
print(x)
print(y)
x[0]=42
print(arr)
y[0]=42
print(arr)

print(c.shape)

arr7 = np.array([1, 2, 3, 4], ndmin=5)      # 5 dimensions array (newaxis)
print(arr7) 
print(arr7.shape)

arr8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr8.reshape(2,3,2).base)      # returns a copy
print(arr8)

arr9 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr2 = arr9.reshape(2, 2, -1)
print(newarr2)
print(c.reshape(-1))

for x in arr:
    print(x, end=' ')
print()
for x in c:
    for y in x:
        print(y, end=' ')


arr10 = np.array([[1,2], [3,4], [5,6]])
for x in np.nditer(arr10):
    print(x, end=' ')
print()
for x in np.nditer(arr10, flags=['buffered'], op_dtypes=['S']): # op_dtypes=['S'] is used to change the data type of elements while iterating 
    print(x, end=' ')                                           # flags=['buffered'] is used to iterate the elements more efficiently
print()

for x in np.nditer(arr10[:, ::2]):        # iterate through every scalar element of the 2nd column of the 2D array skipping 1 element
    print(x, end=' ')
print()


arr11 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr11):
    print(idx, x)
print()
for idx, x in np.ndenumerate(c):
    print(idx, x)

arr12 = np.array([1, 2, 3, 4, 5, 6])
arr13 = np.array([7, 8, 9, 10, 11, 12])
print(np.concatenate((arr12, arr13)))

arr14 = np.array([[1, 2], [3, 4]])
arr15 = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr14, arr15), axis=1))

print(np.stack((arr12, arr13), axis=0))     # stack arrays along the first axis
print(np.stack((arr12, arr13), axis=1))     # stack arrays along the second axis
print(np.hstack((arr12, arr13)))            # stack arrays horizontally
print(np.vstack((arr12, arr13)))            # stack arrays vertically
print(np.dstack((arr12, arr13)))            # stack arrays depth wise

print(np.split(arr12, 2))                   # split the array in 2 parts
print(np.array_split(b, 3))                 # split the array in 3 parts, array_split() allows one of the split to be of different size
print(np.array_split(c,4, axis=1))          # split the array in 4 parts along the y-axis
print(np.hsplit(c, 3))                       # split the array horizontally in 3 parts

print(np.where(arr12 == 4))                 # search an array and return the indexes where the value 4 is present
print(np.where(arr12%2 == 0))               # search an array and return the indexes where the values are even
print(np.searchsorted(arr12, 3))            # search the sorted array and return the index where the value 3 should be inserted
print(np.searchsorted(arr12, 3, side='right')) # search the sorted array and return the index where the value 3 should be inserted
print(np.searchsorted(arr12, [1, 3, 5]))     # search the sorted array and return the indexes where the values 1, 3 and 5 should be inserted
print(np.sort(arr12))                        # sort the array return a copy
print(np.sort(arr3))                         # sort the array of strings
print(np.sort(c))

arr16 = np.array([41, 42, 43, 44])
x = [True, False, True, False]
print(arr16[x])


filter = []
for x in arr16:
    if x > 42:
        filter.append(True)
    else:
        filter.append(False)
print(arr16[filter])

filter1 = arr16 > 42
print(arr16[filter1])