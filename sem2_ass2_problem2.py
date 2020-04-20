#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:48:17 2020

@author: ritambasu
"""

import matplotlib.pyplot as plt
import numpy as np

#defining the right hand side function i.e eular function as given in the question


def f(t,y):
   return (y/t)*(y/t-1)

def exact_sol(t):
    return t/(1+np.log(t))

w=1   
h=0.1
y_num=[]
x=[] #defining this array to append t . It can thought of as an array of 't' (to be created using some loop)
abs_error=[] 
rel_error=[]
t=1


"""use of 1 'while loop' to create the array of y ( the numerically calculated 
solution) , absoute error and relative error w.r.t the exact solution provide in 
the question  """

while t<=2.1:
    y_num.append(w)
    x.append(t)
    abs_error.append(abs(w-exact_sol(t)))
    rel_error.append(abs(w-exact_sol(t))/exact_sol(t))
    w=w+h*f(t,w)
    t=t+h

#Comparison of solutions through plotting

plt.plot(x,y_num,'g',ls='dashed',label="numerical sol")
plt.plot(x,abs_error,ls='dashed',color='orange', marker='o',markersize=6,label="absoute error")
plt.plot(x,rel_error,'ro--',markersize=6,label="relative error")
plt.plot(x,exact_sol(x),'b',label="exact sol")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Euler Method Comparison between (exact vs numerical)')
plt.legend()
plt.show()