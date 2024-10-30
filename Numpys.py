'''import numpy as  np 
#ar=np.array([1,2,3]) #1D array
ar=np.array([[1,2,3],[4,5,6]]) # 2D array
#ar=np.array([[[1,2,3],[4,5,6]], [[7,8,9],[0,1,2]]])
#ar=np.array([1,2,3],ndmin=5)
print(ar)'''


import numpy as np 
ar=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(ar[1,3])   # row 1 and element 3

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0, 1, 2])