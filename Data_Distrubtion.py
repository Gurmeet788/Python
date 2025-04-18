import numpy as np
import matplotlib.pyplot as mp #show the graph into otput
import seaborn as sb #convert the data into graph
# Normal (Gusian) distribution: mean=0, standard devation=2, size=100
normal_data = np.random.normal(loc=0, scale=2, size=100) 
# if you know stndard devation you will understand better;
sb.displot(normal_data)
print(normal_data)
mp.show()