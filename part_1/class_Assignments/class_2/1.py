k = 2
m = 1
p_0 = 2
x_0 = 0
h =2
lamda = 2 

import numpy as np
import matplotlib.pyplot as plt
import math

x = -np.linspace(-3,+3,1000)
p = np.linspace(-3,+3,1000)
X,P = np.meshgrid(x,p)
eqn = X**2 + 0.5*P**2 -2 #different value

x1 = []
y1 = []
omega = math.sqrt(k/m)
A = 1

for i in range(1,45001):
    t = i/1000      #differnt values so as to differentiate better
    x1.append(2*(lamda)*math.cos(omega*t))
    y1.append(-2*(lamda)*m*omega*math.sin(omega*t))


plt.contour(X,P,eqn,[0])
plt.xlim([-6,6])
plt.ylim([-6,+6])
plt.plot(y1,x1)
plt.show()