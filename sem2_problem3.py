#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:01:36 2020

@author: ritambasu
"""

import matplotlib.pyplot as plt
import numpy as np


"""Here we have used the vector methodto to solve simaltenious differential equations
as we have splitted the 2nd order equation into two 1st order equations """

y0=0
dydx0=0#defining initial values 


def f(x,r): # r is an array with r[0]=y and r[1]=z(=dy/dx)
   dydx=r[1]
   dzdx=2*r[1]-r[0]+x*(np.exp(x)-1)
   return np.array([dydx,dzdx])

r=np.array([y0,dydx0])  # initial values of vector r
h=0.001
y_sol=[]
x_sol=[]
x=0 # initial value of x
while x<=1+h:
    y_sol.append(r[0])
    x_sol.append(x)
    k1=h*f(x,r)
    k2=h*f(x+0.5*h,r+0.5*k1)
    k3=h*f(x+0.5*h,r+0.5*k2)
    k4=h*f(x+h,r+k3)
    r=r+(k1+2*k2+2*k3+k4)/6.0
    x=x+h

def y_exact(x):
    return (((np.e)**x)*((x**3)/6+(3/2))+0.5*((np.e)**(-x))-x-2)


#comparison of actual solution with computed solution through plottig  

t=np.arange(0,1,0.01)    
plt.plot(x_sol,y_sol,ls='dashed',color='orange',label="computed solution")
plt.plot(t,y_exact(t),label="actual solution")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solution Using RK4 Method')
plt.legend()
plt.show()


#comparison for higher limits of x
h=0.01
while x<=10+h:
    y_sol.append(r[0])
    x_sol.append(x)
    k1=h*f(x,r)
    k2=h*f(x+0.5*h,r+0.5*k1)
    k3=h*f(x+0.5*h,r+0.5*k2)
    k4=h*f(x+h,r+k3)
    r=r+(k1+2*k2+2*k3+k4)/6.0
    x=x+h
t=np.arange(0,10,0.001) 
plt.plot(x_sol,y_sol,ls='dashed',color='red',label="computed solution")
plt.plot(t,y_exact(t),label="actual solution")
plt.legend()
plt.show() #we can show that for higher values of x these two solutions converge
