# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:10:32 2016

@author: chaws
"""
import numpy as np
from math import fabs

def I(x):
    y=1/(1-np.sin(a/2)**2*np.sin(x)**2)**0.5
    return y

def trap0(f,a,b,n):
    """ Basic trapezium rule . Integrate f (x) over the
    interval from a to b using n strips . """
    h=float(b-a)/n
    s=0.5*(f(a)+f(b))
    for i in range (1,n):
        s=s+f(a+i*h)
    return s*h

def trap1(f,a,b,delta,maxtraps=1024):
    """ Improved trapezium rule . Integrate f (x) over
    interval from a to b , trying to get relative accuracy
    delta . Optional last argument is maximum allowed
    number of trapezia. """
    n=8
    inew=trap0(f,a,b,n)
    iold=-inew # make sure we don ’t terminate immediately
    while(fabs(inew-iold)>delta*fabs(inew)):
        iold=inew
        n=2*n
        if n>maxtraps:
            print " Cannot reach requested accuracy with ", \
            maxtraps , " trapezia"
            return
        inew=trap0(f,a,b,n)
        return inew
t=np.array([])
r=np.arange(0,np.pi/2+np.pi/32,np.pi/32)
print "Amplitude (Pi)\t| Amplitude (Rad)\t| T/T0\t\t\t|" 
for a in r: 
    t=np.append(t,((2/np.pi)*trap1(I,0,np.pi/2,1E-9)))
    #This is a truely inelegant way of making a table but IIRC we don't have prettytable or tabulate.
    print "{:f}\t\t|\t{:5f} \t|\t {:f} \t|".format(a/np.pi,a,t[-1])
