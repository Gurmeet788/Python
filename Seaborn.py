import seaborn as sns
import matplotlib.pyplot as plt

data = {'Day': ['Mon', 'Tue', 'Wed'], 'Sales': [200, 150, 300]} #Day and slaes(Keys)and the array in both are values are the dictinoy in python and like hash map in java 

sns.barplot(x='Day', y='Sales', data=data)
sns.boxenplot(x='Day', y='Sales', data=data)
plt.show()


#seaborn is a libary that is use for data visulaztion with different graph 

#plt is help us to print the graph.
#seaborn change the data into graph from.u