import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
def diffusion(nt, nx, tmax, xmax, nu):
   """
   Returns the velocity field and distance for 1D linear convection
   """
   # Increments
   dt = tmax/(nt-1)
   dx = xmax/(nx-1)

   # Initialise data structures
   u = np.zeros((nx,nt))
   x = np.zeros(nx)

   # Boundary conditions
   u[0,:] = u[nx-1,:] = 1

   # Initial conditions
   for i in range(1,nx-1):
      if(i > (nx-1)/4 and i < (nx-1)/2):
         u[i,0] = 2
      else:
         u[i,0] = 1

   # Loop
   for n in range(0,nt-1):
      for i in range(0,nx-1):
         u[i,n+1] = u[i,n] + nu*(dt/dx**2.0)*(u[i+1,n]-2.0*u[i,n]+u[i-1,n])

   # X Loop
   for i in range(0,nx):
      x[i] = i*dx

   return u, x

def plot_diffusion(u,x,nt):
   plt.figure()
   """ 
   for i in range(0,nt,10):
      plt.plot(x,u[:,i]) """
   plt.plot(x,u[:,70]) 
   plt.xlabel('x (m)')
   plt.ylabel('u (m/s)')
   plt.ylim([0,3.0])
   plt.show()

u,x = diffusion(151, 51, 0.5, 2.0, 0.1)
plot_diffusion(u,x,151)
