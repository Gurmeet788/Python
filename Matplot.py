import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,50]
#line graph
# plt.plot(x,y, marker = 'o',linestyle = '--', color = 'green', label='Cicle') #markers types named are in label
# plt.plot(x,y, marker = '^',linestyle = '--', color = 'green', label='Dimond')
# plt.plot(x,y, marker = 's',linestyle = '--', color = 'green', label='square')
# plt.plot(x,y, marker = '*',linestyle = '--', color = 'green', label='stare') 
# plt.xlabel('X-axis')
# plt.ylabel('y-axis')
# plt.title('Linr graph')
# plt.legend() 
# plt.show()

fig, axs = plt.subplots(1, 2, figsize=(10, 4)) # mean 1 colum 2 row 

# First graph
axs[0].plot([1, 2, 3], [1, 4, 9]) #axs[0] indx 0 1st row 
axs[0].set_title("Graph 1")

# Second graph
axs[1].plot([1, 2, 3], [9, 4, 1]) #axs[1] indx 1 2nd row
axs[1].set_title("Graph 2")

# Adjust layout to prevent overlap
plt.tight_layout()

# Show both graphs in one window
plt.show()