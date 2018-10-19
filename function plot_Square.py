import pylab
import numpy as np
from math import cos, fabs , pi, sin
def g(x):
    n=1; total=term=sin(pi/2*x) # First term
    while fabs(term)>(1.0e-7*fabs (total) + 1.0e-13):
        n += 2 # Advance to next term
        term=sin(n*pi/2*x)/n
        total+=term # Add term to total
    return 4*total/pi
x=np.arange(0,4*pi, pi/16)
print x
y=np.vectorize(g)
z=y(x)
print z
pylab.plot(x,z)
pylab.xlabel ('x')
pylab.title ('A Function g(x)')
pylab.show()
