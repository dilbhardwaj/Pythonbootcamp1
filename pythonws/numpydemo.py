import numpy as np
#creating array using numpy
arr= np.array((7,2,3,4,5))
print(arr)
# print(type(arr))
# print(arr.min())
# print(arr.mean())
# print("before sorting",arr)
arr.sort()
print("after sorting",arr)
#to reverse the sorting by descending 
reversed_arr = arr[::-1]
print(reversed_arr)
arr1=np.flip(arr)



