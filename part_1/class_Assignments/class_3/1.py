import matplotlib.pyplot as plt
import math
import random

x_1 = []
y_1 = []
k = 5
m = 2
A = 2
omega = math.sqrt(k/m)

for j in range(0,4000):
    i = j/1000
    val_x = A*math.sin(omega*i)
    x_1.append(val_x)
    val_y = m*omega*A*math.cos(omega*i)
    y_1.append(val_y)

plt.plot(x_1,y_1)
plt.legend()
plt.show()    