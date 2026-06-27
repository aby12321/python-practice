#lesson 1 = 1D array (A 1D array is like a row of boxes.)

import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)


#lesson 2 = Accessing Elements (Indexing)

import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[1])
print(arr[2])


#lesson 3 = Negative indexing

import numpy as np

arr = np.array([10,20,30,40])

print(arr[-1])
print(arr[-2])


#lesson 4 = Slicing (Slicing means taking a portion of the array.)

import numpy as np

arr = np.array([10,20,30,40])

print(arr[1:4])
print(arr[:3])
print(arr[2:])

#lesson 5= 2D Arrays (a 2D array is like a table.)

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)

#lesson 6= Access Elements in 2D Arrays

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr[0,2])
print(arr[1,2])

# Practice Question =

import numpy as np

arr = np.array([5, 10, 15, 20, 25])

print("First:", arr[0])
print("Last:", arr[-1])
print("Slice:", arr[1:4])