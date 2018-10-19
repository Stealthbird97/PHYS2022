import pylab
import numpy as np
from math import cos, fabs , pi
def g(x):
    n=1; total=term=cos(x) # First term
    while fabs(term)>(1.0e-7*fabs (total) + 1.0e-13):
        n += 2 # Advance to next term
        term=cos(n*x)/(n*n)
        total+=term # Add term to total
    return total
x=np.arange(0,4*pi, pi/16)
#print x
y=np.vectorize(g) # needed to iterate through a numpy array
z=y(x)
#print z
pylab.plot(x,z)
pylab.xlabel ('x')
pylab.ylabel ('g(x)')
pylab.title ('A Function g(x)')
pylab.savefig('g(x).png')
import os
curdir=os.getcwd()
print 'Plot saved in:', curdir
