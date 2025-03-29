import numpy as np
def magnitude(x, y):
    return np.sqrt(x*x + y*y)

def unit(x,y):
    mag = magnitude(x,y)
    return (x/mag, y/mag)

x, y = np.random.randint(100),np.random.randint(100) #using random numpy's libary

z = np.random.rand() #rand function give the random value of 0 to 1 postive if we use randn mean both neg and pos
arr = np.random.randint(5,10,size = 2) #the first two number are range and 3rd is size of array
arr2 = np.random.randint(1,100, size = (3,2)) #2d array

array = np.array([1,2,3,4,5])
print(np.random.choice(array, 5)) #it will print 5 size random array  but the number are choise from array [1,2,3,4,5]
# print(array)
# print(arr)
# print(arr2)
# print(z)
# print(x)
# print(y)
# print("magnitude:", magnitude(x,y))
# print("unit:", unit(x, y))