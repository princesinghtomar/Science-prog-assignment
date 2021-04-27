import numpy as np
import math

BOX_SIZE = 18
VDW_RADIUS = 3.4
N_PARTICLES = 108

def writeout(particles):
    with open('Genconfig.xyz') as f:
        f.write(N_PARTICLES + '\n\n')
        for p in particles:
            f.write("C " +  str(p.x) + " " + str(p.y) + " " + str(p.z) + "\n")

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

def run():
    particles = []
    for i in range(0,N_PARTICLES):
        valid = 0
        while not valid:
            particle = np.random.uniform(0, BOX_SIZE, size=(3))
            valid = 1
            for p in particles:
                if dist(p, particle) >= VDW_RADIUS:
                    pass
                else:
                    valid = 0
                    break
        particles.append(particle)
        print("Accepted : ", len(particles))
    writeout(particles)

run()
