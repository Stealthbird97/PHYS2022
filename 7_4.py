# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 13:57:54 2016

@author: cdh1g15
"""

import numpy as np
def avg(a,b): # diffusuion length
    R=np.sqrt(2*a*b)
    return R
import neutrons as neu
a=1.7E-2
b=21E-2
L=0.0315
N=10000
count=0
for i in range(0,N):
    x=L*np.random.random(); y=L*np.random.random();z=L*np.random.random()
    for j in range(0,neu.neutrons()):
        phi = 2.0*np.pi*np.random.random()
        theta = np.arccos(2.0*np.random.random()-1.0)
        ss=neu.diffusion()
        s=neu.diffusion()*avg(a,b)
        x1=x+s*np.sin(theta)*np.cos(phi)
        y1=y1=x+s*np.sin(theta)*np.sin(phi)
        z1=z+s*np.cos(theta)
        secondary=[x1-x,y1-y,z1-z]
        if secondary[0]<L and secondary[1]<L and secondary[2]<L:
            count+=1
print "Secondaries: ", count, "| Difference: ", count-N 
if count-N>0:
    print "Critical Mass"
else:
   print "Mass Not Critical"   
