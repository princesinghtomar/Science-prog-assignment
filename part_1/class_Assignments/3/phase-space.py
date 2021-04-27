import math
import matplotlib.pyplot as plt
from more_itertools import numeric_range

k=1
m=1

def plott():
    plt.title("Phase Space")
    plt.ylabel("Momentum -->")
    plt.xlabel("Position -->")
    plt.show()

def phase_space(m=0, k=0):
    # hamiltonian = lambda x, p: x * x * k / 2 + p * p / (2 * m)
    range_step=0.1
    legends = []
    def x_p_at_time_t(hamiltonian):
        dt=0.001
        num_iterations=9000
        t = 0
        p = math.sqrt(2 * hamiltonian * m)
        x = 0
        t_list = []
        p_list = []
        x_list = []
        for _ in range(num_iterations):
            x_list = x_list + [x]
            p_list = p_list + [p]
            t_list = t_list + [t]
            dp = x * (-k) * dt
            dx = (p / m) * dt
            t = t + dt
            p = p + dp
            x = x + dx
        return x_list, p_list, t_list

    for val in numeric_range(0, 1, range_step):
        (x_list, p_list, t_list) = x_p_at_time_t(round(val, 1))
        legends.append("H=" + str(val) + ":.02")
        plt.plot(x_list, p_list)
    plott()

phase_space(m, k)
