from numpy import *
arr1 = array ([
    [1,2,3,4,5,6],
    [91,93,94,88,40,20]

])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()

print(arr2)

arr3 = arr2.reshape(4,3)
print(arr3)
print('-----------------------------')
arr4 = arr3.reshape(2,2,3)

print(arr4)
