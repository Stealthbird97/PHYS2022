from numpy import zeros, random
m1=zeros(100, int)
m2=zeros(100, int)
m3=zeros(100, int)
m4=zeros(100, int)
for i in range(1000):
    a=random.normal();b=random.normal();c=random.normal();d=random.normal()
    print a, b, c, d
    avg1=int(10/1*a)
    avg2=int(10/2*(a+b))
    avg3=int(10/3*(a+b+c))
    avg4=int(10/4*(a+b+c+d))
    m1[avg1]=m1[avg1]+1
    m2[avg2]=m2[avg2]+1
    m3[avg3]=m3[avg3]+1
    m4[avg4]=m4[avg4]+1
print m1, m2, m3, m4
from pylab import *
subplot(4,1,1)
title("1 Random Numbers")
bar(arange(0,100,0.1),m1,width=0.1)
ylabel("Frequency")
subplot(4,1,2)
title("2 Random Numbers")
bar(arange(0,100,0.1),m2,width=0.1)
ylabel("Frequency")
subplot(4,1,3)
title("3 Random Numbers")
bar(arange(0,100,0.1),m3,width=0.1)
ylabel("Frequency")
subplot(4,100,4)
title("4 Random Numbers")
bar(arange(0,1,0.1),m4,width=0.1)
ylabel("Frequency")
xlabel("Average of Random Numbers")
subplots_adjust(hspace=0.6)
savefig("5_7.png", dpi=300)
