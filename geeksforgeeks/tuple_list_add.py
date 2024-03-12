tupl = (4,5,6,7,8,9)
list1= [1,2,3,4]
tupl += tuple(list1)
print(tupl)

# Output: (4, 5, 6, 7, 8, 9, 1, 2, 3, 4)
# Explanation: We can add a list to a tuple using the += operator.

ary1= [1,2,3,4]
ary2= [5,6,7,8]
ary1+= ary2
print(ary1)