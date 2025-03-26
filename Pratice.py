import math
def magnitude(x, y):
    return math.sqrt(x*x + y*y)

def unit(x,y):
    mag = magnitude(x,y)
    return (x/mag, y/mag)

x, y = 5,6

print("magnitude:", magnitude(x,y))
print("unit:", unit(x, y))
