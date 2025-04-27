import numpy as np

array = np.array([[1,2,3],[4,5,6]])

print(np.sum(array, axis=1)) # row wise sum
print(np.sum(array, axis=0)) #colum wise sum
print(np.sum(array)) #full array sum