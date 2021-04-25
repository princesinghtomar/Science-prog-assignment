#Related question no #1 at origin which is "0"
import matplotlib.pyplot as plt
import random
import math

y_1 = []

for i in range(1,101):
    if(i%2==1):
        y_1.insert(i,0)
    else:
        I = int(i/2)
        val = math.comb(i,I)
        y_1.insert(i,val/(math.pow(2,i)))

y_2 = []

for i in range(1,100):
    val = 0
    for j in range(1,10001):
        pos_1 = 0
        for k in range(1,i+1):
            pos_1 = pos_1 + math.floor(random.choice([-1,1]))
        if( pos_1 == 0):
            val = val + 1
    y_2.insert(i,val/10000)

plt.figure(figsize=(20,20))
plt.ylabel("Probability -->")
plt.xlabel("N -->")
plt.title('Graph')
plt.plot(y_2,label='Simulated')
plt.plot(y_1,label='Calculated')
plt.legend()
plt.show()