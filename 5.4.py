from numpy import zeros, random
m=zeros(10, int)
for i in range(1000):
    n=int(10*random.random())
    m[n]=m[n]+1
print m
from pylab import *
bar(arange(0,1,0.1),m,width=0.1)
ylabel("Frequency")
xlabel("Random Value")
savefig("5_4.png", dpi=300) 
