import numpy as np

Array = np.array([1,2,3,4])
reshape = Array.reshape(2,2, order='A') #order = 'C' row major order = 'F' colum major order = 'A' is Any of them  but defult = 'C'

print(Array)
print(reshape) # reshape the Array into what dimension you want