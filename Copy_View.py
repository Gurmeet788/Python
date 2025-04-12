import numpy as np

Array = np.array([1,2,34])
Copy = Array.copy()#copy function can not change.
view = Array.view() #view function changes in orginal.
Copy[0] = 99
view[0] = 93
print(Array)
print(view)