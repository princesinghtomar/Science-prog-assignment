from math import sqrt
import re
import random

# some other lists
molecule_num = []
molecule = []
charges = []

# coordinates
z_coords = []
y_coords = []
x_coords = []

# restrictions
Lz=27.1759
Ly=22.406
Lx=23.623

k = 332.1

def read(destination):
    f_psf = open(destination , "r")
    psf_lines = f_psf.readlines()
    f_psf.close()
    return psf_lines

psf_lines = read("./ICES.psf")

for x in psf_lines[6:1302]:
    temp = x.strip()
    molapp = re.sub('\s+' , ' ' , temp).split(' ')[5]
    chapp = re.sub('\s+' , ' ' , temp).split(' ')[6]
    molnuapp = re.sub('\s+' , ' ' , temp).split(' ')[2]
    molecule.append(molapp)
    charges.append(chapp)
    molecule_num.append(molnuapp)

temp_charges = []
for ch in charges:
    temp_charges.append(float(ch))
charges = temp_charges.copy()

temp_num_mol = []
for i in molecule_num:
    temp_num_mol.append(int(i))
molecule_num = temp_num_mol.copy()

pdb_lines = read("./starting_config_300k.pdb")


for x in pdb_lines[:-1]:
    temp = x.strip()
    y_capp = re.sub('\s+' , ' ' , temp).split(' ')[6]
    z_capp = re.sub('\s+' , ' ' , temp).split(' ')[7]
    x_capp = re.sub('\s+' , ' ' , temp).split(' ')[5]
    y_coords.append(y_capp)
    z_coords.append(z_capp)
    x_coords.append(x_capp)

# coordinated work
temp_coor = []
for x_c in x_coords:
    temp_coor.append(float(x_c))
x_coords = temp_coor.copy()
temp_coor = []

for y_c in y_coords:
    temp_coor.append(float(y_c))
y_coords = temp_coor.copy()
temp_coor = []

for z_c in z_coords:
    temp_coor.append(float(z_c))
z_coords = temp_coor.copy()

print(len(x_coords))

def get_dist(x1,y1,z1 , x2 , y2 , z2):
    rx = abs(x1 - x2)
    dist = 0
    # boundary conditions
    rx = (rx - (((round(rx/Lx))* Lx)))
    dist = dist + (rx)*(rx)
    ry = abs(y1 - y2)
    #bondary conditions
    ry = (ry - (((round(ry/Ly))* Ly)))
    dist = dist + (ry)*(ry)
    rz = abs(z1 - z2)
    #bondary conditions
    rz = (rz - (((round(rz/Lz))* Lz)))
    dist = (rz)*(rz) + dist
    dist = sqrt(dist)
    return dist

def get_electro(q1 , q2 , r):
    res = k
    res *= q1
    res *= q2
    res /= r
    return res

r_arr = []
tot_energy = 0
energy = 0
for i in range(0,1296):
    main_charge = charges[i]
    main_mol_num = molecule_num[i]
    if energy:
        energy = 0
    main_z = z_coords[i]
    main_y = y_coords[i]
    main_x = x_coords[i]
    for j in range(i,1295):
        zc = z_coords[j+1]
        yc = y_coords[j+1]
        xc = x_coords[j+1]
        ch = charges[j+1]
        r = get_dist(main_x , main_y , main_z , xc , yc , zc)

        mn = molecule_num[j+1]
        if main_mol_num == mn:
            continue

        r_arr.append(r)

        energy = get_electro(main_charge , ch , r) + energy

        if molecule[j+1] == molecule[i] and molecule[i] == 'OT':
            energy = ((582000/(r**12)) - (595/(r**6))) + energy


    tot_energy = energy + tot_energy

print('Total Potential Energy: {}'.format(tot_energy))

prev_energy = tot_energy
prev_z_coords = z_coords
prev_y_coords = y_coords
prev_x_coords = x_coords
cur_z_coords = []
cur_y_coords = []
cur_x_coords = []

print(len(x_coords))
# # prev_x_coords[:10]
# [x + random.uniform(-2,2) for x in prev_x_coords[:10]]

for step in range(10):
    cur_energy = 0
    cur_mol_num = 0
    cur_z_coords = prev_z_coords
    cur_y_coords = prev_y_coords
    cur_x_coords = prev_x_coords

    for it in range(0,len(cur_x_coords)):
        if molecule_num[it] is not cur_mol_num:
            delta = random.uniform(-0.01, 0.01)
            cur_mol_num = molecule_num[it]

        cur_z_coords[it] = (delta + Lz + cur_z_coords[it] )%Lz
        cur_y_coords[it] = (delta + Ly + cur_y_coords[it] )%Ly
        cur_x_coords[it] = (delta + Lx + cur_x_coords[it])%Lx
    
    energy = 0
    for i in range(0,1296):
        main_mol_num = molecule_num[i]
        main_charge = charges[i]
        if energy:
            energy = 0
        main_z = cur_z_coords[i]
        main_y = cur_y_coords[i]
        main_x = cur_x_coords[i]
        for j in range(i,1295):
            zc = cur_z_coords[j+1]
            yc = cur_y_coords[j+1]
            xc = cur_x_coords[j+1]
            ch = charges[j+1]
            r = get_dist(main_x , main_y , main_z , xc , yc , zc)
            mn = molecule_num[j+1]
            if main_mol_num == mn:
                continue

            energy = get_electro(main_charge , ch , r) + energy

            if molecule[j+1] == molecule[i] and molecule[i] == 'OT':
                energy = (580000/(r**12)) - (525/(r**6)) + energy


        cur_energy = energy + cur_energy
    print(step , "energy is " , cur_energy)

    if cur_energy < prev_energy:
        prev_z_coords = cur_z_coords
        prev_y_coords = cur_y_coords
        prev_x_coords = cur_x_coords
        prev_energy = cur_energy

