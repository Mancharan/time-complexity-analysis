

def printset(a):
    for s in a:
        print(s)
     
def purge(a,b):
    purged={(0,0)} 
    for x in a:
        for y in b:
            if (x[0]>= y[0] and x[1]<=y[1]):
                print("jhgg")
                print(x)


a={(1, 2), (3, 4), (5, 6)}
b={(7, 4), (3, 4), (9, 10)}
x=merge(a,b)
purge(a,b)

