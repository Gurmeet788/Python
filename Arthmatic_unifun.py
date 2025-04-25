import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([5,6,7])

print("ADD:", np.add(array1,array2))
print("SUB:", np.subtract(array1,array2))
print("MULI:", np.multiply(array1,array2))
print("DIVI:", np.divide(array1,array2))
print("Scalar mul:", np.multiply(array2,2))

#These all are univesal functions they are fast as compare to normal python function. 
#NumPy universal functions (ufuncs) are written in C for speed and performance.