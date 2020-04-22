#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 21:08:20 2020

@author: ritambasu
"""

import numpy as np
import matplotlib.pyplot as plt
candidate_sol=[] # candidate solutions for different v's as it's element 
y_vf=[] # stores the y(x_f) for different y'[0]=v guesses
#v_guess=[]
g=10
initial_value_of_x=0
final_value_of_x=10
def f(x,r): # r is an array with r[0]=y and r[1]=z(=dy/dx)
   dydx=r[1]
   dzdx=-g
   return np.array([dydx,dzdx])
for v in np.arange(30.,90.,1):
    trial_sol_for_particular_v=[]
    r=np.array([0.0,v])  # initial values y[0]=0,and y'[0]=v
    h=0.001
    x=initial_value_of_x 
    x_f=final_value_of_x
    x_sol=[]
    while x<=x_f+h:
       trial_sol_for_particular_v.append(r[0])
       x_sol.append(x)
       k1=h*f(x,r)
       k2=h*f(x+0.5*h,r+0.5*k1)
       k3=h*f(x+0.5*h,r+0.5*k2)
       k4=h*f(x+h,r+k3)
       r=r+(k1+2*k2+2*k3+k4)/6.0
       x=x+h
    y_vf.append(r[0])
    #v_guess.append(v)
    candidate_sol.append(trial_sol_for_particular_v)
y_vf=np.array(y_vf)    
x_sol=np.array(x_sol)

"""comparision between y(xf=10) for differentv's  
w.r.t to y(xf) given in the problem """
index_of_min=np.argmin(abs(y_vf - 0))


#plotting
plt.plot(x_sol,candidate_sol[index_of_min],
           ls='dashed',label="numerical solution")
#exct solution plotting
plt.plot(x_sol,-0.5*g*x_sol*x_sol + 50*x_sol, ls=':', label="exact solution")


#plotting candidate solutions
for i in range(index_of_min - 10, index_of_min + 10 , 4):
    plt.plot(x_sol,candidate_sol[i],label="candidate solution")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.xlim(0.,10.)
plt.title('Shotting Method')
plt.legend()
plt.show()
