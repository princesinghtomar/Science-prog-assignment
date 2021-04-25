# mean displacement
import matplotlib.pyplot as plt
import random
import math

y_1 = []

y_2 = []

for i in range(1,100):
    val = 0
    for j in range(1,120001):
        pos_1 = 0
        for k in range(1,i+1):
            pos_1 = pos_1 + math.floor(random.choice([-1,1]))
        val += pos_1
    y_2.insert(i,val/120000)
    #print(val)
    y_1.insert(i,0)

plt.figure(figsize=(20,20))
plt.ylabel("mean displacement -->")
plt.xlabel("N -->")
plt.title('Graph')
plt.plot(y_2,label='Simulated')
plt.plot(y_1,label='Calculated')
""" 
plt.ylabel("Frequency -->")
plt.xlabel("deviation -->")  # for histogram
plt.hist(y_2)
"""
plt.legend()
plt.show()