import numpy as np

Array_1d = np.array([1,2,3,4])
Array_2d = np.array([[1,2,3,4],[5,6,7,8]])
Array_3d = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])

print(Array_1d.shape)
print(Array_2d.shape) # shape function tell about the shape of array like how many row and cloume are in and the dimenmision of array

Arr = np.array([1,5,7,4],ndmin=2) #ndmin function make the dimenstion like 1 int n number of deminsion
print(Arr.shape)