import numpy as np

#python function
def add(x,y):
    return x+y

#add1 function now behave np universal function they are fast runtime wise.
add1 = np.frompyfunc(add,2,1)

array = np.array([1,2,3])
array1 = np.array([4,5,6])

print(add1(array,array1))

#np.frompyfunc() turns a regular Python function into a NumPy universal function (aka ufunc), so it can work element-wise on NumPy arrays — even if the original function doesn’t support that.

#np.frompyfunc(func, nin, nout)

# func	Your Python function
# nin	Number of input arguments
# nout	Number of outputs

