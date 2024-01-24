def reverse():
    c = arr[d:] + arr[:d]
    return c

arr= [1,2,3,4,5,6,7,8,9,10,11,12]
d = 3
print(reverse())


# The slice arr[d:] represents the elements starting from index d to the end of the array.
# The slice arr[:d] represents the elements from the beginning of the array up to index d.
# Essentially, this line rotates the array to the left by d positions.