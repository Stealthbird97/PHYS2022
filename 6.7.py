import numpy as np
def f(y,t):
    return -y + np.cos(w*t)
def odestep(f,y,t,dt ):
    ya=f(y,t) #slope at A
    b=y+dt*ya #B Position
    yb=f(b,t+dt) #Slope at B
    return y+dt*0.5*(ya+yb) #Return revised B position.
t=0; y=0; dt=0.01
tf=2*np.pi; nsteps=int(tf/dt)
print "t | y"
print t, y
w1=[];w2=[];w3=[]
tt=[]
w=1
for i in range(nsteps):
    y=odestep(f,y,t,dt)
    tt.append(t)
    t=(i+1)*dt
    w1.append(y)
t=0; y=0; dt=0.01
w=2
for i in range(nsteps):
    y=odestep(f,y,t,dt)
    t=(i+1)*dt
    w2.append(y)
w=3
for i in range(nsteps):
    y=odestep(f,y,t,dt)
    t=(i+1)*dt
    w3.append(y)
import pylab as pl
pl.subplot(3,1,1)
pl.plot(tt,w1)
pl.subplot(3,1,2)
pl.plot(tt,w2)
pl.subplot(3,1,3)
pl.plot(tt,w3)
pl.show()
