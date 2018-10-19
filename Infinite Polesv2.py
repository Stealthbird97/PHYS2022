import numpy as np
import pylab as pl
r=100.0
s=10000.0
a=np.array([r+s])
aa=0
while abs((a[-1])-aa)>1.0e-12*a[-1]: #Compares the difference of the last two numbers and checks if is small enough
    aa=a[-1]
    rnn=r+s*a[-1]/(s+a[-1])
    a=np.append(a,rnn)
print "Value for R tending to Infinity is: " , a[-1], "Ohm"
m=np.size(a) # Number of interations to infinity
n=np.arange(0,m-1,1) #-1 as r to infinity in the last element of array which will cause a zero error in the log functions.
b=np.array([])
for o in n:
    b=np.append(b,a[o]-a[-1])
c=np.log10(b)
d=np.log(b)
pl.plot(n+1, c, label='$Log_{10}(R_n-R_\infty)$')
pl.plot(n+1, d, label='$Log_{2}(R_n-R_\infty)$')
pl.legend(loc='upper right')
pl.xlabel('n iterations')
pl.title('Infinite Length Circuit')
pl.ylabel('$Log(\Omega)$')
pl.savefig('Circuitplot.png')
import os
curdir=os.getcwd()
print 'Plot saved in: ', curdir
           
