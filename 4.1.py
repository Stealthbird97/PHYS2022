import numpy as np
def I(x):
    y = (x**4*(1-x)**4)/(1+x**2)
    return y

def trap0(f,a,b,n):
    """ Basic trapezium rule. Integrate f(x) over the
    interval from a to b using n strips . """
    h=float (b-a)/n
    s =0.5*(f(a)+f(b))
    for i in range (1,n):
        s=s+f(a+i*h)
    return s*h

def I2(x):
    y=np.exp(-x**2)
    return y
v=2*trap0(I2,0,5.3,10)
print v
    
    
