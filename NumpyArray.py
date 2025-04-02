import numpy as np

#1D Array
array_1 = np.array([1,2,3,4])
# print(array_1)

# 2D Array
array_2 = np.array([[1,2,3],[4,5,6]])
#print(array_2)

# 3D Array
array_3 = np.array([[[1,2],[4,5]],[[7,8],[8,9]]])
# print(array_3)
# print(array_3.ndim) this function tell the dim number 

# Note: An element showes the no of colum and 1st barket show the number of dim and middle barket show the row

#Just Give an array an diman number it will change it 

array = np.array([[1,2,3,4,5],[1,1,1,1,1]], ndmin=3) #ndmin variable use for dimension number if we make 2d array and give ndmin variable number less than 2 it will print 2 mean it take largest dimension
# print(array)
# print(array.ndim)

print(array_1[0]) #print first value
print(array_1[-1]) #print last value mean reverse
mark = array_1 > 2  
print(array_1[mark]) #boolean indx greater than 2 value in array printed 

print (array_2[0][-1]) #print first row last value

