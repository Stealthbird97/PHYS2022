from numpy import *
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
ea=array(ea)
na=array(na)
dn=array(dn)
def theory(e,w): #Calculates Theoretical Values
    x = 1.467e7/(w*w/4+(e-1232)**2)
    return x
#w=raw_input('w:')
#w=sqrt((4*(1.467e7/na[na.size/2-1])-(ea[ea.size/2-1]-1232)**2))
w= 119
print "using ", w, " as w"
th = array(theory(ea,w))
pl.plot(ea,na, label='Experimental')
pl.errorbar(ea,na,dn)
pl.ylabel('n(E)')
pl.xlabel('E')
pl.plot(ea,th, label='Theoretical')
pl.legend(loc='upper right')
pl.title("w=115")
pl.show()

    
    
