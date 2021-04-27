import math
import matplotlib.pyplot as plt

k=1
m=1

def plott(t_list, x_sq_list):
    plt.figure(figsize=(20,20))
    plt.title("Mean Square Displacement vs Time")
    plt.ylabel("Displacement Square")
    plt.plot(t_list, x_sq_list)
    plt.xlabel("Time")
    plt.show()

def mean_square_displacement(m=0, k=0, num_iterations=9000,dt=0.001):
    hamil=0.5
    def x_at_time_t(hamiltonian):
        t = 0
        p = math.sqrt(2 * hamiltonian * m)
        x = 0
        t_list = []
        p_list = []
        x_list = []
        for i in range(num_iterations):
            x_list = x_list + [x]
            t_list = t_list + [t]
            p_list = p_list + [p]
            dp = x * (-k) * dt
            dx = (p / m) * dt
            x = dx + x
            p = dp + p
            t = dt + t
        return x_list, t_list

    x_list, t_list = x_at_time_t(hamil)
    x_sq_list = [x**2 for x in x_list]
    plott(t_list, x_sq_list)

mean_square_displacement(m, k)
