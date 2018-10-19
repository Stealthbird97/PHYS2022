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
def h(x): # h(x)=cos(x)+cos(3x^3)/n^3+cos(5x^5)/5^3+...+
    n=1; total=term=sin(pi/2*x) # First term
    while fabs(term)>(1.0e-7*fabs (total) + 1.0e-13):
        n += 2 # Advance to next term
        term=sin(n*pi/2*x)/n
        total+=term # Add term to total
    return 4*total/pi
x=np.arange(0,4*pi, pi/32)
#print x
y=np.vectorize(g) # needed to iterate through a numpy array
z=y(x)
u=np.vectorize(h) # needed to iterate through a numpy array
v=u(x) 
#print z
pylab.plot(x,z, label='g(x)')
pylab.plot(x,v, label='h(x)') #additional function
pylab.legend(loc='upper right')
pylab.xlim(0, 4*pi)
pylab.xticks((0, pi/2, pi, 3*pi/2, 2*pi, 5*pi/2, 3*pi, 7*pi/2, 4*pi),
    ('$0$', '$0.5\pi$', '$\pi$', '$1.5\pi$', '$2\pi$', '$2.5\pi$', '$3 \pi$', '$3.5\pi$', '$4 \pi$') )
pylab.xlabel ('x')
pylab.title ('Fourier Series Functions')
pylab.savefig('Fourierplot.png')
import os
curdir=os.getcwd()
print 'Plot saved in:', curdir
