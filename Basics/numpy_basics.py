# -*- coding: utf-8 -*-

import numpy as np

# Source: https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/
# Creating array object

arr = np.array([[1, 2, 3],
                [4, 2, 5]])

arr3 = np.array([[1, 2, 3], [4, 2, 5], [8, 9, 0]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions arr: ", arr.ndim)
#print("No. of dimensions arr3: ", arr3.ndim)

# Printing shape of array 
print("Shape of array arr: ", arr.shape)
#print("Shape of array arr3: ", arr3.shape)

# Printing size (total number of elements) of array
print("Size of array arr: ", arr.size)
#print("Size of array arr3: ", arr3.size)

print("Array stores elements of type arr: ", arr.dtype)

# Print all rows, printing column 1:3
print("Print all rows, printing column 1:3:")
print(arr3[:, 1:3])
# Print rows starting at 1, printing column 1:3
print("Print rows starting at row1, printing column 1:3:\r")
print(arr3[1:, 1:3])
# Print rows ending at 1, printing column 1:3
print("Print rows ending before row1, printing column 1:3:\r")
print(arr3[:1, 1:3])