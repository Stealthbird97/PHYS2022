import numpy as np
import pylab as pl
#Import Data
f=open('data1.txt','r',)
ea=[]; na=[]; dn=[];
for line in f:
    estr,nstr,errstr=line.split()
    ea.append(float(estr))
    na.append(float(nstr))
    dn.append(float(errstr))
f.close()
#create numpy arrays
ea=np.array(ea)
na=np.array(na)
dn=np.array(dn)
def theory(e,w): #Calculates Theoretical Values
    x = 1.467e7/(w*w/4+(e-1232)**2)
    return x
#w= 154 # choose W
def discrepancy(w): #Finds Discrepancy
    x=np.array(theory(ea,w)) # calculates theoretical values
    ri=na-x # finds ri
    risidual=(ri/dn)**2 #
    s=np.sum(risidual)
    return s
#Trial and Error...
w=np.arange(0,160,1) # creates a range of values to trial
dis=np.vectorize(discrepancy) # enables iteration through array elements
z=dis(w) # creates array of discrepencies for each tried w value.
print  'Minimum Discrepency = ', np.amin(z), ', w = ', np.argmin(z) # prints the index and value of the minimum discrepency
#using minimise function
import minimise as mm
m=mm.gmin(discrepancy,100,200)
print m

