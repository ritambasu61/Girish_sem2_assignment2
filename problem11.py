#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:18:53 2020

@author: ritambasu
"""

import matplotlib.pyplot as plt
import numpy as np


"""Here we have used the vector methodto to solve simaltenious differential equations"""

#defining initial values 
u10=3
u20=-1
u30=1


#defining the vector function f(t,u)
def f(t,u): # u is an array with u[0]=u1(t),u[1]=u2(t),u[2]=u3(t)
   f0=u[0]+(2*u[1])-(2*u[2])+np.exp(-t)
   f1=u[1]+u[2]-2*np.exp(-t)
   f2=u[0]+(2*u[1])+np.exp(-t)
   return np.array([f0,f1,f2])

u=np.array([u10,u20,u30])  # initial values of vector u
h=0.001
u1=[]
u2=[]
u3=[]
t_arr=[]
t=0 # initial value of t
while t<=1+h:
    u1.append(u[0])
    u2.append(u[1])
    u3.append(u[2])
    t_arr.append(t)
    k1=h*f(t,u)
    k2=h*f(t+0.5*h,u+0.5*k1)
    k3=h*f(t+0.5*h,u+0.5*k2)
    k4=h*f(t+h,u+k3)
    u=u+(k1+2*k2+2*k3+k4)/6.0
    t=t+h


#comparison of actual solution with computed solution through plottig  
   
plt.plot(t_arr,u1,label="u1(t)")
plt.plot(t_arr,u2,label="u2(t)")
plt.plot(t_arr,u3,label="u3(t)")
plt.xlabel('t')
plt.ylabel('u(t)')
plt.title('Solving simaltenious differential equations using RK4 Method')
plt.legend()
plt.show()


