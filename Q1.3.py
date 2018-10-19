a=range(1,11) # range(10) if number 0 to 9
b=[x*x for x in a]
c=[x*x*x for x in a]
for x in a:
    print a[x-1], b[x-1], c[x-1] #remove (-1) if numbers 0 to 9
