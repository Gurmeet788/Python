import numpy as np
import matplotlib.pyplot as mp
import seaborn as sb
# λ = 3, on avrage
x = np.random.poisson(lam=3, size=4)
print(x)

#suppose the customer on average 3 customer comes at shopes in every 10 min tells us in every 10 min how many people come on avrage 4 time mean 10 * 4 = 40 n 40 min how many people come

#let's pilot it
sb.histplot(x,bins= np.max(x),edgecolor = 'Black')

mp.title("on average 3 customer comes at shopes in every 10 min")
mp.ylabel("Frequncy/Quantity")
mp.xlabel("No of customer per 10 min interverl")
mp.grid(True)
mp.show()