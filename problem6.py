#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Apr 18 21:03:35 2020

@author: ritambasu
"""

import numpy as np
import matplotlib.pyplot as plt

h=0.1 
t=np.arange(0+h,10,h)
A=np.zeros((t.size,t.size))
for i in range (t.size):
    for j in range (t.size):
        if j==i-1 or j==i+1:
            A[i][j]=1 #A is the matrix of coefficient of the linear equations
        elif j==i:
            A[i][j]=-2
b=-10*h*h*np.ones(t.size)
L=np.tril(A,k=0) 
U=np.triu(A,k=1) #This matrix contains the lower triangular elements of A
l=np.linalg.inv(L) #inverse of matrix L
def y(m):
    z=np.zeros(t.size) #initial guess of solution
    for j in range (m): #j is the no of iteration to used to plot candidate solutions
        z=np.dot(l,(b-np.dot(U,z)))
    z=np.insert(z,[0,t.size],[0,0]) #inserting the value of y at boundary points
    return z #return the sol by gauss-seidal method after m iteration
t1=np.arange(0,10+h,h)
ite_no=np.array([800,1000,1200,1500,2000])
for j in ite_no:
    plt.plot(t1, y(j)) #plotting of candidate solutions
plt.plot(t1, y(5000))
def g(t):
    return 50*t-5*t*t #analytical sol of differential eq
t=np.arange(0,10,0.01)
plt.plot(t,g(t)) #plotting analytical solution
plt.xlabel('t', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.title('t vs y graph')
plt.legend(['iteration no=800','iteration no=1000','iteration no=1200','iteration no=1500','iteration no=2000','true numerical solution','analytical solution'],fontsize=10,loc='upper left')
plt.show()
