#importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

'''This code will solve the steady heat equation on a L_x by L_y domain
with a prescribed grid size'''

#assigning values to constants
A = 150 # all x along L_y
B = 200 # all y along L_x
C = 50 # allx along y = 0
T_inf = 300
h = 250
k = 5
a = 1
b = -k/h
g_w = T_inf

#grid characteristics
L_x = 0.8
N_x = 4
h_x = L_x/N_x

L_y = 0.6
N_y = 3
h_y = L_y/N_y

#Create the temperature grid
T = np.zeros((N_y + 2,N_x + 2)) #need two on either side for both for ghost CVs

#Start at side 1 (bottom) to implement Dirichlet BC
T[N_y+1, :] = 2*C - T[N_x,:]

#Side 3 (top) to implement Dirichlet BC
T[0, :] = 2*A - T[1,:]

#Side 2 (right) to implement Dirichlet BC
T[1:N_y+1, N_x+1] = 2*B - T[1:N_y+1,N_x]

#Side 4 (left) to implement Robin BC
T[1:N_x, 0] = (2*b + a*h_x)**-1 * (2*h_x*g_w + (2*b - a*h_x)*T[1:N_x, 1])

#We will now iterate through the values prescribed using the Gauss-Seidel method. 
#This requires use of a while loop to iterate until we reach a certain prescribed tolerance.
tolerance = 0.0001
iterate = True #If this condition holds we continue to iterate

#Store the value of the current temperature
T_curr = np.empty([N_y+2, N_x+2])
for i in range(0, N_y + 2):
    for j in range(0, N_x+2):
        T_curr[i,j] = T[i,j]


count = 0

while(iterate is True):
    count = count + 1
    print("Starting Iteration ", count)

    # First populate the interior values
    for i in range(1, N_y + 1):
        for j in range(1, N_x+1):
            T[i,j] = (h_y**2 * (T[i+1, j] + T[i-1, j]) + h_x**2 * (T[i,j-1] + T[i,j+1]))/(2*(h_x**2 + h_y**2))
    
    #Now doing Side 1 boundary
    for i in range(1, N_x+1):
        T[N_y+1, i] = 2*C - T[N_y,i]

    #Now doing Side 2 boundary
    for i in range(1, N_y+1):
        T[i, N_x+1] = 2*B - T[i, N_x]
    
    #Now doing Side 3 boundary
    for i in range(1, N_x+1):
        T[0,i] = 2*C - T[1,i]
    
    #Side 4 (left) to implement Robin BC
    for i in range(1, N_y+1):
        T[i, 0] = (2*b + a*h_x)**-1 * (2*h_x*g_w + (2*b - a*h_x)*T[i, 1])

    #Now we calculate the error to see if we are within the desired tolerance
    error = np.abs(T - T_curr)
    max_e = np.max(error)

    #Store the value of the current temperature to compare for the next iteration
    for i in range(0, N_y + 2):
        for j in range(0, N_x+2):
            T_curr[i,j] = T[i,j]
    print('The max error for this iteration is: ', max_e)
    
    #If we are within the tolerance, this condition determines whether looping continues
    if(max_e < tolerance):
        iterate = False # We stop iterating
print('The temperature at (2,2) is:', T[2,2])