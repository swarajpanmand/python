from numpy import random
import numpy as np
print(random.randint(100))
print(random.rand())
print(random.randint(100, size=(5)))    
print(random.randint(100, size=(3, 5)))
print(random.rand(5))
print(random.choice([3,5,8]))
print(random.choice([3,5,8], size=(3, 5)))

print(random.choice([1,2,3,4], p=[0.1, 0.3, 0.6, 0.0], size=(100)))
print(random.choice([1,2,3,4], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)))

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)                     # shuffle the array makes changes in the original array
print(arr)
print(random.permutation(arr))          # permutation returns a new array