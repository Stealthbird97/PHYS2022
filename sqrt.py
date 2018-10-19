def square_root( x ):
    y=x
    z=0
    while y*y!=x:
        z=y #improvement
        print y, y*y
        y =0.5*(y+x/y)
        if y==z: #improvement
            break
    return y

def sinexoverx( x ):
    if x ==0:
        return 1
    else:
        return sin (x )/ x
