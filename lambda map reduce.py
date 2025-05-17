cube=lambda x:x*x*x
sq=lambda x: x*x
def add1(f,val):
    # add=(cube(2)+f(val))
    return cube(2)+f(val)

print(add1(sq,5))

def isEven(n):
    return n%2==0
l=[1,4,9,5,6,7,2,4]
g=list(map(lambda x:x*x,filter(isEven,l)))
print(g)

from functools import reduce
d=reduce(lambda x,y:x+y,l)
print(d)
