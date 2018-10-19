def f(y,t):
    return -y + 1.0
def odestep(f,y,t,dt ):
    ya=f(y,t) #slope at A
    b=y+dt*ya #B Position
    yb=f(b,t+dt) #Slope at B
    return y+dt*0.5*(ya+yb) #Return revised B position.
t=0; y=0; dt=0.0001
tf=2.0; nsteps=int(tf/dt)
print "t | y"
print t, y
for i in range(nsteps):
    y=odestep(f,y,t,dt)
    t=(i+1)*dt
    print t, y
