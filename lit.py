def max(L):
    y=L[1]
    t=L[1]
    for x in L:
        if(y>x):
            y=x
        if(t<x):
            t=x
    return y,x
print(max([1,2,3,4,5]))
