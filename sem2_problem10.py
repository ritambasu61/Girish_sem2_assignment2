#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:14:48 2020

@author: ritambasu
"""

import matplotlib.pyplot as plt
def f(t,x):
   return (1/(t*t+x*x))
y=1
h=1
t_f=3.5*(10**6)
soln=[]
x=[]
t=0
while t<=t_f+h:
    
    k1=h*f(t,y)
    k2=h*f(t+0.5*h,y+0.5*k1)
    k3=h*f(t+0.5*h,y+0.5*k2)
    k4=h*f(t+h,y+k3)
    y=y+(k1+2*k2+2*k3+k4)/6.0
    t=t+h
    if t<=100:
       soln.append(y)
       x.append(t)
       
    
print("Value of x(t) at t=",t_f," is= ",y)


#plotting
plt.plot(x,soln,label="numerical sol")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Graph of solution using RK4 method')
plt.legend()
plt.show()