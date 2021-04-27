import numpy as np
import matplotlib.pyplot as plt

temperature = np.arange(1, 5, 0.05)
N = 20

def plott(temperature, magnetisation):
    plt.figure(figsize=(20,20))
    plt.ylabel("Magnetisation")
    plt.scatter(temperature, magnetisation)
    plt.xlabel("Temperature")
    plt.show()

def get_magnetisation_temperature(N, temperature, trials, J):
    magnetisation = np.zeros(len(temperature))
    magnet = 0
    for j in range(0,len(temperature)):
        if magnet:
            magnet = 0
        model = np.random.choice([-1, 1], size=N)
        for i in range(0,trials):
            for rnd in range(0,N):
                index = np.random.randint(0, N)
                right_n,left_n= (1 + rnd) % N, (-1 + rnd) % N
                effect = model[left_n] + model[right_n]
                if(np.random.rand()< np.exp(-model[index] * effect / temperature[j]) or model[index] * effect < 0):
                    model[index] = -model[index]
                else:
                    model[index] = model[index]
            magnet = sum(model) + magnet
        magnetisation[j] = magnet / (N * trials)
    plott(temperature, magnetisation)

J = 1
trials = 1024
get_magnetisation_temperature(N, temperature, trials, J)
