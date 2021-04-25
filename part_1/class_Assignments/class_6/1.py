import matplotlib.pyplot as plt
import random
import math

val = 0
y_1 = []
arr = []
standard_deviation = 0
sd = []
n = 20
trials = 10001

for i in range(1,trials):
    value = 0
    val = 0
    for i in range(1,n):
        x_pos = random.uniform(0,1)
        y_pos = random.uniform(0,3)
        if ( 3*x_pos*x_pos >= y_pos ):
            val += 1
    value = (3*val/n)
    arr.insert(i,value)
    standard_deviation += math.pow(((value)-1),2)
    val = math.sqrt(standard_deviation/n)
    sd.insert(i,val)
    y_1.insert(i,1)

plt.title('Graph')
print("val",val)
#plt.plot(y_1,label='Calculated')
#plt.plot(arr,label='Simulated')
plt.plot(sd,label='Stanard Deviation')
plt.legend()
plt.show()
