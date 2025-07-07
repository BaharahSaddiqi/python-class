import math , sys
from module import *
from math import sin,pi as s,p

print(math.pi)
def sin(x):
    if 2*x==pi:
        return 0.9999999
    else:
        return  None
pi=3.14  
print(sin(pi/2))  
print(math.sin(math.pi/2))
for name in dir(math):
    print(name, end="\t")