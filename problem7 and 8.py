#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:01:07 2020

@author: ritambasu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import solve_bvp
"""To argue why the given solution of the diff equ. by using 
scipy.integrate.solve_ivp() gives correct result we plot the 
exact solution and absolute error both matches perfectly"""
def my_ivp(f , exact_sol ,t0 ,tf, y0, h):
    
    t=np.arange(t0,tf,h)
    soln=solve_ivp(f,[t0,tf],[y0],t_eval=t)
    plt.plot(t,soln.y[0],marker='*',markersize=3,label="Numerical Solution")
    plt.plot(t,exact_sol(t),label="Exact Solution")
    plt.plot(t,abs(exact_sol(t)-soln.y[0]),label="Absolute Error")
    plt.xlabel('t', fontsize=13)
    plt.ylabel('y(t)', fontsize=13)
    plt.title('Solution Using solve_ivp()')
    plt.legend()
    plt.show()
def my_bvp(f ,bc ,t0 ,tf ,y0 ,yf):
    x=np.linspace(t0 , tf , 5)
    # initially choosen y'(t) in the y[1] array and initial guess of y in the y[0]
    y=np.zeros((2 , x.size)) + 1
    sol_bvp = solve_bvp(f, bc, x, y)
    
    x_plot = np.linspace(t0 , tf , 100)
    y_plot=sol_bvp.sol(x_plot)[0]
    
    plt.plot(x_plot, y_plot,marker='*',markersize=3,label='numerical solution')
    plt.legend()
    plt.xlabel("t", fontsize=13)
    plt.ylabel("y(t)", fontsize=13)
    plt.show()

#problem 7a
def f(t,y):
    return t*(np.exp(3*t))-2*y
def exact_sol(t):
    return np.exp(3*t)*(t-0.2)/5.0+np.exp(-2*t)/25.0
t0=0.0
tf=1.0
y0=0.0
h=0.01
my_ivp(f , exact_sol ,t0 ,tf, y0, h)


#problem 7b
def f(t,y):
    return 1 - (t-y)**2 
def exact_sol(t):
    return t + 1/(t-3.0)
t0=2.0
tf=3.0
y0=1.0
h=0.01
my_ivp(f , exact_sol ,t0 ,tf, y0, h)

#problem 7c
def f(t,y):
    return 1+(y/t)
def exact_sol(t):
    return 2*t+t*np.log(t)
t0=1.0
tf=2.0
y0=2.0
h=0.01
my_ivp(f , exact_sol ,t0 ,tf, y0, h)

#problem 7d
def f(t,y):
    return np.cos(2*t)+np.sin(3*t)  
def exact_sol(t):
    return np.sin(2*t)/2.0 - np.cos(3*t)/3.0 + 4/3
t0=0.0
tf=1.0
y0=1.0
h=0.01
my_ivp(f , exact_sol ,t0 ,tf, y0, h)




    
#problem 8a
t0 , tf = 1 , 2
y0 , yf =0 , np.log(2)
def f(x,y):
    
    # y is an array with y[0]=y and y[1]=z(=dy/dt)
    return np.array([y[1],-np.exp(-2*y[0])])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])

my_bvp(f ,bc ,t0 ,tf ,y0 ,yf)



#problem 8b

t0 , tf = 0 , (np.pi)/2.
y0 , yf =1 , np.e
def f(x,y):
    return np.array([y[1], y[1]*np.cos(x) - y[0]*np.log(y[0])])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])
my_bvp(f ,bc ,t0 ,tf ,y0 ,yf)



#problem 8c

t0 , tf = (np.pi)/4. , (np.pi)/3.
y0 , yf =2**(-0.25) , 0.5*(12**(0.25))
def f(x,y):
    return np.array([y[1], - (2 * y[1]**3 + y[0]**2 * y[1]) /np.cos(x) ])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])
my_bvp(f ,bc ,t0 ,tf ,y0 ,yf)



#problem 8d

t0 , tf = 0 , np.pi
y0 , yf = 2 , 2
def f(x,y):
    return np.array([y[1], 0.5 - 0.5 * y[1]**2 - 0.5 * y[0] * np.sin(x)])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])
my_bvp(f ,bc ,t0 ,tf ,y0 ,yf)
