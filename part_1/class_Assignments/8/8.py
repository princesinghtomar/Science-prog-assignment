import numpy as np
import matplotlib.pyplot as plt

# solver class
class solver():
    def __init__(self,initial_N1, initial_N2, params, time, intervals):
        self.time_interator = np.linspace(0, time, intervals)
        self.init_N1 = initial_N1
        self.init_N2 = initial_N2
        self.final_N2 = []
        self.final_N1 = []

    # simulator
    def simulate(self,params):
        for t in range(0,len(self.time_interator)):
            self.final_N1.append(self.init_N1)
            self.final_N2.append(self.init_N2)
            dt = -self.time_interator[0] + self.time_interator[1]

            dN1 =  (params["r"]*self.init_N1*(1-self.init_N1/params["k"]) - params["alpha"]*self.init_N1*self.init_N2) * dt
            dN2 = (params["beta"]*self.init_N1*self.init_N2 - params["c"]*self.init_N2) * dt

            self.init_N1 = self.init_N1 + dN1
            self.init_N2 = self.init_N2 + dN2

    # Returning functions
    def ret_final_N2(self):
        return self.final_N2

    def ret_time_itr(self):
        return self.time_interator

    def ret_final_N1(self):
        return self.final_N1

# Details of models 
N1_init_list = (16, 13)
N2_init_list = (2, 3)
r_list = (1.4, 2.2)
alpha_list = (0.4, 0.4)
beta_list = (0.14, 0.16)
c_list = (0.5, 0.4)
k_list = (20, 20)

for i in range(0,len(N1_init_list)):

    N1_init = N1_init_list[i]
    N2_init = N2_init_list[i]
    intervals = 500
    time = 100

    # parameters of Predator-Prey model
    params = {
       "c": c_list[i],
       "beta": beta_list[i],
       "alpha": alpha_list[i],
       "k": k_list[i],
       "r": r_list[i]
    }

    # Solver Class Details
    solver_class = solver(N1_init, N2_init, params, time, intervals)
    solver_class.simulate(params)
    N1_list = solver_class.ret_final_N1()
    N2_list = solver_class.ret_final_N2()
    time_interator = solver_class.ret_time_itr()

    # print details of the model
    print("N1(0): " + str(N1_init))
    print("N2(0): " + str(N2_init))
    print(params)
    print("x ------------------------------------------------------- x")

    # ploting procedure
    plt.figure(figsize=(10,10))

    plt.plot(time_interator, N1_list)
    plt.plot(time_interator, N2_list)

    plt.title("Prey Predator Model")
    plt.ylabel("Population -->")
    plt.xlabel("Time Period -->")
    plt.legend(["Prey", "Predator"])
    plt.show()
