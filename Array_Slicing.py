import numpy as np
#Basic Syntax:
#array[start:stop:step]

#slicing 1d
array_1d = np.array([1,2,3,4,5])
#print(array_1d[0:1])  #mean 0 to 1 indx , 1 is exslive, : mean not included
# print(array_1d[0::3]) #:: mean i am skping the stop in stament direct jump the step 0::3 mean start from 0 indx and skip 2 value reach 3 it will print [1,4]

#slicing 2d

array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d[0:2,0:2]) #The first 0:2 tell about row 0 and 1 and 2nd 0:2 tell about colum 0 and 1 it will print [[1,2],[4,5]] [1,2] from row 0 and colum 0 and 1 and [4,5] row 1 colum 0 and 1


#Step if -1 traverse in reverse order

print(array_1d[3:0:-1]) # satrt from 3 to 1

print(array_1d[::]) #it mean whole array startdefet 0 stop array.size - 1 and step by def 1 


#3d
arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(arr3d[:, 1, :])

# #Here’s the breakdown of the slicing:

# arr3d[:, 1, :]:

# The first colon (:) refers to all layers (in this case, two layers: arr3d[0] and arr3d[1]).

# The 1 refers to the second row in each layer (because row indices start from 0).

# The last colon (:) refers to all columns in the selected row.

# Explanation:
# arr3d[0] is the first layer: [[1, 2], [3, 4]]

# arr3d[1] is the second layer: [[5, 6], [7, 8]]

# When you access arr3d[:, 1, :], you're selecting the second row from both layers:

# From arr3d[0], the second row is [3, 4].

# From arr3d[1], the second row is [7, 8].