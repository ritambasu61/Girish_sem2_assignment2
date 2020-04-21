#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Apr 9 11:22:33 2020

@author: ritambasu
"""

import matplotlib.pyplot as plt
import numpy

def f(t,x):
    return (x+x*x)/t

#defining RK4 function to compute y(t+h) for given values of t
def RKUT4(t,y,h):  
    k1=h*f(t,y)
    k2=h*f(t+0.5*h,y+0.5*k1)
    k3=h*f(t+0.5*h,y+0.5*k2)
    k4=h*f(t+h,y+k3)
    y=y+(k1+2*k2+2*k3+k4)/6.0
    return y

#initial t
t2=3.
t1=1.
delta=10**(-4) # accuracy as mentioned in the question

y=-2 # initial value of y(t)
h=0.01  # initial value of step_size taken

#defining array to append the numerical solutions
y_arr=[]
t_arr=[]
count1=0
count2=0
t=t1
while t<=t2 + h:
  y1 = RKUT4(t+h , RKUT4(t,  y , h) , h)  # evaluating y[t+2h] by first at t then at t+h
  y2 = RKUT4(t , y , 2 * h)
  row = 30 * h * delta/abs(y1 - y2) #evaluating y[t+2h] by a single step t to t+2h
  h_prime = row**(1/4.) * h #relation between h and h' through row
  if row**(1/4.)>1:
      h=h_prime
      continue   
      count1=count1+1
  
  else:
    h=h_prime
    y_arr.append(y)
    t_arr.append(t)
    y=RKUT4(t , y , h)
    count2=count2+1
  t=t+h
# plotting exact and numerical one
t=numpy.arange(t1,t2+3,0.1)
plt.plot(t_arr,y_arr,ls='dashed',marker='*',markersize=8,label="Numerical solution with Sample Points")
plt.plot(t,2*t/(1 - 2*t),label="analytic solution solution") 
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('RK4 Method with adaptive step-size control')
plt.legend()
plt.show()
print('count2=',count2,'count1=',count1)
"""results shows that count 1=0 i.e row >1 i.e h_prime >h does not happen for the give
initial stepsize(h)=0.01.So, for our initial value of h for all cases get updated
by the arequied accurate h (which is esimated to match the given accuracy)
"""