# mean Squared displacement
import matplotlib.pyplot as plt
import random
import math

y_1 = []

y_2 = []

for i in range(1,101):
    val = 0
    for j in range(1,10001):
        pos_1 = 0
        for k in range(1,i+1):
            pos_1 = pos_1 + math.floor(random.choice([-1,1]))
        val += ((pos_1)*(pos_1))
    y_2.insert(i,val/10000)
    y_1.insert(i,i)

plt.figure(figsize=(20,20))
plt.ylabel("Mean squared displacement -->")
plt.xlabel("N -->")
plt.title('Graph')
plt.plot(y_2,label='Simulated')
plt.plot(y_1,label='Calculated')
plt.legend()
plt.show()