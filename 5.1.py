from numpy import zeros , random
m= zeros (10 ,int)
for i in range (1000):
    n= random . randint(10)
    m[n]=m[n ]+1
print m
from pylab import *
bar(range(10),m,width=1,align ='center')
xticks(range(10))
ylabel("Frequency")
xlabel("Random Value")
savefig("5_3.png", dpi=300)
