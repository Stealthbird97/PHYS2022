import pylab
import numpy as np
from math import cos, fabs , pi, sin
def g(x):
    n=1; total=term=cos(x) # First term
    while fabs(term)>(1.0e-7*fabs (total) + 1.0e-13):
        n += 2 # Advance to next term
        term=cos(n*x)/(n*n)
        total+=term # Add term to total
    return total
def h(x):
    f=10
    n=1; total=term=sin(2*pi*f*x) # First term
    while fabs(term)>(1.0e-10*fabs (total) + 1.0e-13):
        n += 1 # Advance to next term
        term=sin(2*pi*(2*n-1)*f*x)/(2*n-1)
        total+=term # Add term to total
    return 4*total/pi
x=np.arange(0,4*pi, pi/2)
#print x
y=np.vectorize(g) # needed to iterate through a numpy array
z=y(x)
u=np.vectorize(h) # needed to iterate through a numpy array
v=u(x) 
#print z
pylab.plot(x,z, label='g(x)')
pylab.plot(x,v, label='h(x)') #additional function
pylab.legend(loc='upper right')
pylab.xticks(np.arange(min(x), max(x)+pi/2, pi/2))
pylab.xlabel ('x')
pylab.title ('Fourier Series Functions')
pylab.savefig('plot.png')
import os
curdir=os.getcwd()
print 'Plot saved in:', curdir
