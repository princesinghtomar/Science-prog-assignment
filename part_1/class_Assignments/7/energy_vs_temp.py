import numpy as np
import matplotlib.pyplot as plt

temperature = np.arange(1, 5, 0.05)
N = 20

def plott(temperature, energy):
    plt.ylabel("Energy")
    plt.scatter(temperature, energy)
    plt.xlabel("Temperature")
    plt.show()

def get_energy_temperature(N, temperature, trials, J):
    energy = np.zeros(len(temperature))
    energy_temp = 0
    for i in range(0,len(temperature)):
        if energy_temp:
            energy_temp = 0
        model = np.random.choice([-1, 1], size=N)
        for j in range(0,trials):
            nrg = 0
            for rnd in range(0,N):
                index = np.random.randint(0, N)
                right_n,left_n= (1 + rnd) % N, (-1 + rnd) % N
                cost =  (model[right_n] + model[left_n])*model[index]
                if(cost < 0 or np.random.rand() < np.exp(-cost / temperature[i])):
                    model[index] = -model[index]
                else:
                    model[index] = model[index]
            for rnd in range(0,N):
                right_n,left_n= (1 + rnd) % N, (-1 + rnd) % N
                nrg = nrg + -J * model[rnd] * (model[right_n] + model[left_n])
            energy_temp = (nrg/2) + energy_temp
        energy[i] = energy_temp / (N*trials)
    plott(temperature, energy)

J=1
trials=1024
get_energy_temperature(N, temperature, trials, J)
