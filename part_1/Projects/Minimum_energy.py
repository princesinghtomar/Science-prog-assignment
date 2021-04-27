import numpy as np
from math import sqrt, inf
import pandas as pd
from copy import deepcopy

BOX_SIZE = 18
VDW_RADIUS = 3.4
N_PARTICLES = 108
EPSILON = 0.238

def dist(pos1, pos2):
    x2 = pos2[0]
    y2 = pos2[1]
    z2 = pos2[2]
    x1 = pos1[0]
    y1 = pos1[1]
    z1 = pos1[2]
    dy = abs(y2-y1)
    dy = min(BOX_SIZE-dy,dy)
    dx = abs(x2-x1)
    dx = min(BOX_SIZE-dx,dx)
    dz = abs(z2-z1)
    dz = min(BOX_SIZE-dz,dz)
    return math.sqrt(dz*dz + dx*dx + dy*dy)

def load_config():
    with open('init.xyz') as buff:
        content = buff.read()
        particles=[]
        content = content.split('\n')[2:]
        for i in range(0,len(content)):
            pos = list(map(lambda x: float(x), content[i].split()[1:]))
            if len(pos) > 0:
                particles.append(pos)
        return particles

config = load_config()

def compute_energy(config):
    net_energy = 0
    for p1 in range(0,len(config)):
        for p2 in range(0,len(config)):
            if config[p1]!=config[p2]:
                r = dist(config[p1],config[p2])
                B = (VDW_RADIUS/r)**6
                A = (VDW_RADIUS/r)**12
                net_energy = 4*EPSILON*(A-B) + net_energy
    return net_energy/2

E = compute_energy(config)

def check(config):
    valid = 1
    min_dist = inf
    for p1 in range(0,len(config)):
        for p2 in range(0,len(config)):
            if config[p1] != config[p2]:
                r = dist(config[p1],config[p2])
                min_dist = min(r,min_dist)
                if VDW_RADIUS > r:
                    valid = 0
    return min_dist, valid


print("Configuration's Energy : ", E)

def minimize_energy(config):
    min_config = config
    min_energy = compute_energy(min_config)
    n_tries = 1000
    print("Energy minimizing is being undertaken : ")
    for i in range(0,n_tries):
        print("Try " + str(i))
        new_config = deepcopy(min_config)
        for p in range(0,len(new_config)):
            new_config[p][0] = new_config[p][0] + np.random.uniform(-0.01, 0.01)
            new_config[p][1] = new_config[p][1] + np.random.uniform(-0.01, 0.01)
            new_config[p][2] = new_config[p][2] + np.random.uniform(-0.01, 0.01)
            new_config[p][0] = new_config[p][0] % BOX_SIZE
            new_config[p][1] = new_config[p][1] % BOX_SIZE
            new_config[p][2] = new_config[p][2] % BOX_SIZE

        (min_dist, valid) = check(new_config)
        if not valid:
            continue
        else:
            new_energy = compute_energy(new_config) 
            if min_energy > new_energy :
                min_energy,min_config = new_energy,new_config
    
    return min_energy ,min_config

E, config = minimize_energy(config)

print("Minimized Energy is: ", E)
print(check(config))
