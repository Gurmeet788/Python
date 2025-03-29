import numpy as np
def magnitude(x, y):
    return np.sqrt(x*x + y*y)

def unit(x,y):
    mag = magnitude(x,y)
    return (x/mag, y/mag)

x, y = np.random.randint(100),np.random.randint(100) #using random numpy's libary


print(x)
print(y)
print("magnitude:", magnitude(x,y))
print("unit:", unit(x, y))