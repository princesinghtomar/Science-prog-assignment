import random
import math
import matplotlib.pyplot as plt
import numpy as np

def function_1(x,y):
    val = (math.pow(x,2))*3
    return val

def function_2(x, y):
    val = y*(math.pow(x,2))
    return val

def part1(N, T, graph=1):
    act_val = 1
    s = 0
    differ = 1  # (b-a) = 1 - 0 = 1
    if graph == 1:
        I_plot0 = []
        N_plot0 = []
        for N1 in range(1, 100):
            if s:
                s = 0
            for n in range(N1):
                r2,r1 = random.random(),random.random()
                v = function_1(r1, r2)
                s = s + (differ * v)
            val = s / N1
            N_plot0.append(N1)
            I_plot0.append(val)
        temp_va = [act_val for i in range(N1)]
        plott2(N_plot0, I_plot0, temp_va)
    plotT = []
    plotI = []
    for t in range(T):
        s = 0
        for n in range(N):
            r2,r1 = random.random(),random.random()
            v = function_1(r1, r2)
            s = s + (differ * v)
        val = s / N
        plotI.append(val)
        plotT.append(t)
    temp_va2 = np.array(plotI)
    mean = np.mean(temp_va2)
    standard_dev = np.std(temp_va2)
    print("Standard Deviation -    " + str(standard_dev) + "\t Mean Value - " + str(mean))
    if graph == 1:
        temp_va = [1 for i in range(T)]
        plott(plotT,plotI,temp_va)
    else:
        return standard_dev


def part2(N, T, graph=1):
    differ = 1  # (b-a) = 1 - 0 = 1
    act_val = 1 / 6
    s = 0
    if graph == 1:
        N_plot0 = []
        I_plot0 = []
        for N1 in range(1, 100):
            if s:
                s = 0
            for n in range(N1):
                r2,r1 = random.random(),random.random()
                v = function_2(r1, r2)
                s = s + (differ * v)
            val = s / N1
            I_plot0.append(val)
            N_plot0.append(N1)
        temp_va = [act_val for i in range(N1)]
        plott2(N_plot0, I_plot0, temp_va)
    plotI = []
    plotT = []
    act_val = 1 / 6
    s = 0
    for t in range(T):
        if s :
            s = 0
        for n in range(N):
            r1,r2 = random.random(),random.random()
            v = function_2(r1, r2)
            s = s + (differ * v)
        val = s / N
        plotI.append(val)
        plotT.append(t)
    temp_va2 = np.array(plotI)
    mean = np.mean(temp_va2)
    standard_dev = np.std(temp_va2)
    print("Standard Deviation - " + str(standard_dev) + "\t Mean Value - " + str(mean))
    if graph == 1:
        temp_va = [1 / 6 for i in range(T)]
        plott(plotT,plotI,temp_va)
    else:
        return standard_dev

def plott2(N_plot0,I_plot0,temp_va):
    plt.figure(figsize=(20,20))
    plt.plot(N_plot0, I_plot0)
    plt.plot(N_plot0, temp_va)
    plt.show()

def plott(numberline,standard_dev,sq_n):
    plt.figure(figsize=(20,20))
    plt.plot(numberline, standard_dev)
    plt.plot(numberline, sq_n)
    plt.legend(["Simulated Value", "Actual Value"])
    plt.show()

if __name__ == "__main__":
    std_dev1 = []
    std_dev2 = []
    part1(1000, 100)
    part1(20, 100)
    part2(1000, 100)
    part2(20, 100)
    sq_n = []
    numberline = []
    for n in range(1, 100):
        std_dev2.append(part2(n, 1000, graph=0))
        std_dev1.append(part1(n, 1000, graph=0))
        sq_n.append(1 / (n ** (0.5)))
        numberline.append(n)
    plott(numberline,std_dev1,sq_n)
    plott(numberline,std_dev2,sq_n)
