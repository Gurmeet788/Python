import numpy as np
import matplotlib.pyplot as mp
x= np.random.uniform(0,10,10)
print(x)

mp.hist(x,bins= 10,color= 'red',edgecolor = "black")
mp.title("Uniform Distrubiton")
mp.xlabel("Random number from a to b")
mp.ylabel("Quantity of random number")
mp.grid(True)
mp.show()

#unfiorm distrbution gentrate float number from a to b like as rand() function but rand function genrate from 0 to 1 float but in unfiorm it genrate a to b range