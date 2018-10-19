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
L=0.14
N=10000
count=0
for i in range(0,N):
    position=L*np.random.random()
    for j in range(0,neu.neutrons()):
        if (np.random.random()>0.5):
            vector=1
        else:
            vector=-1
        secondary=position+vector*avg(a,b)
        if 0<secondary<L:
            count+=1
print "Secondaries: ", count, "| Difference: ", count-N 
if count-N>0:
    print "Critical Mass"
else:
   print "Mass Not Critical"   
