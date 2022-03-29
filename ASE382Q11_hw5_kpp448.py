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
h = np.array([0.1, 0.005, 0.001, 0.0005]) #distance between grid points
k = np.array([0.01, 0.005, 0.001, 0.0005]) #distance between time steps
c = 1 #value of c in determining courant number
N = 1/k #arbitrary number of time steps for now

#variables for looping through everything
iterate = True
hval = 0
kval = 0

#the following loop will iterate through time using values prescribed above
#while(iterate is True):
x = np.linspace(0,1,int(1/h[hval] + 1)) #gives us domain of integration (i.e. number of rows)
ex = np.zeros((np.size(x),2)) #create the vector with which we solve to the end
#lw = np.zeros((np.size(x),2))
#bw = np.zeros((np.size(x),2))
sigma = c*k[kval]/h[hval] #prescribe a value of k for this iteration based off sigma

for i in range(len(x)):
    ex[i,0] = np.sin(4*np.pi*x[i])
    #lw[i,0] = np.sin(4*np.pi*x[i])
    #bw[i,0] = np.sin(4*np.pi*x[i])

