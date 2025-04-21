import numpy as np
import matplotlib.pyplot as mp

number,pro,exp = 10,0.5,100 
np.random.seed(42)
data = np.random.binomial(number,pro,exp)

print(data[:20])
mp.hist(data, bins=np.max(data[:20]), edgecolor='black')
mp.title("Binomial Distribution: n=10, p=0.5")
mp.xlabel("Number of Successes (out of 10)")
mp.ylabel("Frequency")
mp.grid(True)
mp.show()

#sppose the coin is flop 
#we are fliping the coin 10 time per expriment and it is fear problity 0.5 chanse of head and 0.5 chanse of tail 
#we are doing 100 experiment Answer Each one shows how many "successes" occurred in that trial (like how many heads you got in 10 flips)

