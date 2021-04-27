import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(0, 25, 0.05)
prob = []
x = np.linspace(-1, 1, 25)
dt = 0.05
D = 0.01
dx = 0.08
prob.append([0]*len(x))
prob[0][12] = 1
legend_1 = []
for i in range(0,t.size):
    prob.append([0]*x.size)
    for posit in range(0,x.size):
        if posit == 24 or posit == 0:
            prob[1+i][posit] = 0
            continue
        prob[1+i][posit] = prob[i][posit] + D*dt/(math.pow(dx,2)) * (prob[i][1+posit] + prob[i][posit-1] - 2*prob[i][posit])

for i in range(0, len(prob), 10):
    dist = prob[i]
    if dist[12] - 0.1 > 0:
        plt.plot(x, dist)
        legend_1.append("t=" + str(t[i]))

plt.legend(legend_1)
# plt.figure(figsize=(20,20))
plt.ylabel("probability -->")
plt.xlabel("position -->")
plt.show()
legend_1 = []

for i in prob:
    dist = i
    if dist[12] - 0.1 > 0: 
        plt.plot(x, dist)

plt.legend(legend_1)
linspac10 = np.linspace(0, 10, 10)
linspac100 = np.linspace(0, 10, 100)
plt.ylabel("probability -->")
linspac1000 = np.linspace(0, 10, 1000)
plt.xlabel("position -->")
plt.show()

t = [linspac10, linspac100, linspac1000]

dy = dx
y = np.linspace(-1, 1, 25)

def plot(Dx, Dy, t):
    prob = [None]*(len(t)+1)
    for i in range(0,len(t)+1):  
        prob[i] = ([np.zeros(25) for j in range(0,25)])
    prob[0][12][12] = 1

    for i in range(0,len(t)):
        for j in range(0,len(x)):
            for k in range(0,len(y)):
                if j == 0 or j == 24:
                    prob[1+i][k][j] = 0
                    continue
                if k == 24 or k == 0:
                    prob[1+i][k][j] = 0
                    continue
                prob[1+i][k][j] = prob[i][k][j]
                prob[1+i][k][j] = prob[1+i][k][j] + Dx*dt/(math.pow(dx,2))*(prob[i][k][j+1] - prob[i][k][j]*2 + prob[i][k][j-1])
                prob[1+i][k][j] = prob[1+i][k][j] + Dy*dt/(math.pow(dy,2))*(prob[i][k+1][j] - prob[i][k][j]*2 + prob[i][k-1][j])
                prob[1+i][k][j] = prob[1+i][k][j] + Dx*Dy*(math.pow(dt,2))/(math.pow(dx,2))*(math.pow(dy,2)) * (prob[i][k-1][j-1] + prob[i][1+k][j-1] + prob[i][k-1][1+j] + prob[i][1+k][1+j] - prob[i][k][j]*4)
    plt.figure(figsize=(20,20))
    map_extent = [-1, 1, -1, 1]
    plt.imshow(prob[len(t)], extent = map_extent, cmap="inferno")
    if Dx > Dy: 
        plt.title("Dx greater than Dy and "+ str(len(t)) + " timesteps")
    elif Dx == Dy: 
        plt.title("equal Dx, Dy and "+ str(len(t)) + " timesteps")
    elif Dx < Dy: 
        plt.title("Dy greater than Dx and "+ str(len(t)) +" timestamps")
    plt.show()

np.seterr('raise')
(Dx, Dy) = (0.01, 0.01)
for ti in range(0,len(t)): plot(Dx, Dy, t[ti])

np.seterr('raise')
(Dx, Dy) = (0.01, 0.005)
for ti in range(0,len(t)): plot(Dx, Dy, t[ti])

np.seterr('raise')
(Dx, Dy) = (0.005, 0.01)
for ti in range(0,len(t)): plot(Dx, Dy, t[ti])
