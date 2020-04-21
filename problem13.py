#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  Apr 14 10:05:51 2020

@author: ritambasu
"""

import matplotlib.pyplot as plt
import numpy as np


"""Here we have used the vector methodto to solve simaltenious differential equations
as we have splitted the 2nd order equation into two 1st order equations """

y0=1
dydt0=0#defining initial values 


def f(x,r): # r is an array with r[0]=y and r[1]=s(=dy/dx)
   dydx=r[1]
   dsdx=(2/t)*(r[1]-r[0]/t)+t*np.log(t)
   return np.array([dydx,dsdx])

r=np.array([y0,dydt0])  # initial values of vector r
h=0.001
y_sol=[]
t_sol=[]
t=1 # initial value of t
while t<=2+h:
    y_sol.append(r[0])
    t_sol.append(t)
    r=r+h*f(t,r)
    t=t+h

def y_exact(t):
    return 7*t/4+(t**3)*np.log(t)/3-3*(t**3)/4


#comparison of actual solution with computed solution through plottig  

x=np.arange(1,2,0.001)    
plt.plot(t_sol,y_sol,ls='dashed',color='orange',label="computed solution")
plt.plot(x,y_exact(x),label="actual solution")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Eular Method for 2nd order differential equations')
plt.legend()
plt.show()


#comparison for higher limits of t
h=0.001
while t<=1000+h:
    y_sol.append(r[0])
    t_sol.append(t)
    r=r+h*f(t,r)
    t=t+h
x=np.arange(0,1000,0.01) 
plt.plot(t_sol,y_sol,ls='dashed',color='red',label="computed solution")
plt.plot(x,y_exact(x),label="actual solution")
plt.legend()
plt.show() #we can show that for higher values of x these two solutions converge"""
