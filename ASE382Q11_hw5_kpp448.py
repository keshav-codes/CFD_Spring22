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
h = np.array([0.01, 0.005, 0.001, 0.0005]) #distance between grid points
k = np.array([0.01, 0.005, 0.001, 0.0005]) #distance between time steps
c = 1 #value of c in determining courant number
N = 1/k #arbitrary number of elements in x for now

#the following loop will iterate through time using values prescribed above
iterate = True
i = 1
j = 1
while(iterate is True):
    x = np.linspace(0,1,1/h(i))
#Part 1: Euler Explicit Upwind