import numpy as np
import pylab as pl
def I(x):
    y=1/(np.cos(x)-np.cos(a))**0.5
    return y
a=np.pi/2
x=np.arange(0,a,a/24)
z=I(x)
pl.plot(x,z)
def I2(x):
    y=1/(1-np.sin(a/2)**2*np.sin(x)**2)**0.5
    return y
a=np.pi/2
x=np.arange(0,a,a/24)
z=I2(x)
pl.plot(x,z)
pl.show()
