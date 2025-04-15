import numpy as np

array = np.array([1,2,3,4])

#np.random.shuffle()
#This method randomly rearranges the items in a NumPy array in place (it changes the original array).

np.random.shuffle(array)

print(array)

array1 = np.array([1,5,7,8,9])

# If you want a new shuffled copy (without changing the original):
# Use np.random.permutation()

Shafaled = np.random.permutation(array1)
print(array1)
print(Shafaled)