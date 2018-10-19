# -*- coding: cp1252 -*-
def trap0(f,a,b,n):
    """ Basic trapezium rule. Integrate f(x) over the
    interval from a to b using n strips . """
    h=float (b-a)/n
    s =0.5*(f(a)+f(b))
    for i in range (1,n):
        s=s+f(a+i*h)
    return s*h
def trap1 (f,a,b,delta , maxtraps=512):
    """ Improved trapezium rule. Integrate f(x) over
    interval from a to b, trying to get relative accuracy
    delta. Optional last argument is maximum allowed
    number of trapezia. """
    n=8
    inew= trap0(f,a,b,n)
    iold=- inew # make sure we don’t terminate immediately
    while ( fabs(inew - iold)> delta * fabs( inew )):
        iold= inew
        n=2*n
        if n> maxtraps:
            print " Cannot reach requested accuracy with", \
            maxtraps , " trapezia"
        return
    inew= trap0 (f,a,b,n)
    return inew
print trap1(x^2,0,1,1E-7)
