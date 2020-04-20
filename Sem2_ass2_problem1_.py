#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:58:51 2020

@author: ritambasu
"""

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.optimize as so

#by implicit method(Backword Integration Method):

#1st problem:

#exact solution:
x_exact= np.arange(0,1.01,0.01)
y_exact= np.exp(1-(9*x_exact))
plt.title('Problem 1')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_exact, y_exact,'b', label='Exact Solution')


h= 0.05
x= np.arange(0,1.05,0.05)
y= np.zeros(21)
y[0]= np.e 
for i in range(20):
	y[i+1]= y[i]/(1+9*h)

plt.plot(x,y,'r',label='Numerical Solution ')
plt.legend()
plt.show()


#2nd problem:



h=0.05
x= np.arange(0,1.05,0.05)
y= np.zeros(21)
y[0]= 1/3

"""
to find the recursion relation
we have used newton ramphson method to find the roots of eular relation
at ith step . As newton rempson will give roots close to our choice of initial 
guess of the root. So, here I have use the my guess as the previous value of y
i.e y[i] to find y[i+1] as close to it as possible for the continuty of the 
curve tobe mentained. So that this method can be used in general.


"""
for i in range(20):
	a  = x[i+1]
	b  = y[i]
	def f(y):
		return(20*h*(y-a)**2+y-b-(2*h*a))	
	y[i+1]= so.newton(f,b) #reason behind choosing b(=y[i])is cleared in the previous documentation
                             
                              
plt.title('Problem 2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'r',label='Numerical Solution ')
plt.legend()
plt.show()