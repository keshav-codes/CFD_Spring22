#Homework 5, Keshav Prathivadi (EID: xxxxxx)
#ASE 382Q-11

'''This code will create the baseline solver for three different methods:
- Euler Explicit Upwind
- Lax-Wendroff
- Beam Warming'''

#Import initial libraries
import numpy as np
import matplotlib.pyplot as plt

#Establishing initial characteristics
h = np.array([0.1, 0.005, 0.001]) #distance between grid points
sigma = np.array([0.1, 0.25, 0.5]) #prescribe values of sigma for stability
n = np.array([1, 10, 100, 1000])
c = 1 #value of c in determining courant number

#variables for looping through everything
iterate = True
hval = 0
sigval = 0
nval = 0

#the following loop will iterate through time using values prescribed above
while(iterate is True):
    #establishing initial values
    sig_curr = sigma[sigval]
    h_curr = h[hval]
    k = sig_curr*h_curr
    n_curr = n[nval]
    print('The value of n is: ',n_curr)
    print('The value of h is: ',h_curr)
    print('The value of k is: ',k)
    print('The value of sigma is: ',sig_curr)

    #creating variables for bookkeeping
    x = np.linspace(0,1,int(1/h[hval] + 1)) #gives us domain of integration (i.e. number of rows)
    up = np.zeros((np.size(x),2)) #create the vector with which we solve to the end
    for i in range(len(x)):
        up[i,0] = np.sin(4*np.pi*x[i]) #populate in initial values

    #Now that values have been changed, we can work on iterate forward in time
    n_steps = n_curr/k
    print(n_steps)
    for i in range(len(n_steps) - 1):
        for j in range(len(x) - 2):
            up[j+1, 1] = up[j+1, 0] - sig_curr*(up[j+1, 0] - up[j, 0])
        for j in range(len(x)):
            up[j, 0] = up[j, 1]
            up[j, 1] = 0
    print(up)

