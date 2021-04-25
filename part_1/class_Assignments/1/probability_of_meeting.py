# Question number 1 ( meeting Drunker wala )
import matplotlib.pyplot as plt
import random
import math

y_1 = []

for i in range(1,101):
    val = math.comb(2*i,i)
    y_1.insert(i,val/(math.pow(4,i)))

y_2 = []

for i in range(1,100):
    val = 0
    for j in range(1,10001):
        pos_1 = 0
        pos_2 = 0
        for k in range(1,i+1):
            pos_1 = pos_1 + math.floor(random.choice([-1,1]))
            pos_2 = pos_2 + math.floor(random.choice([-1,1]))
        if( pos_1 == pos_2):
            val = val + 1
    y_2.insert(i,val/10000)

plt.figure(figsize=(20,20))
plt.ylabel("P(N) -->")
plt.xlabel("N -->")
plt.title('Graph')
plt.plot(y_1,label='Calculated')
plt.plot(y_2,label='Simulated')
plt.legend()
plt.show()