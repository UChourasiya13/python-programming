# rewriting a function
from support import *



#decorators are function which we can modify the
#current functioning of a function

def smart_div(func):
    def inner(m,n):
        if m<n:
            m,n=n,m
        return func(m,n)
    return inner        


a = int(input("enter a value of a: "))
b = int(input("enter a value of b : "))
c = div(a, b)
div1 = smart_div(div)
d = div1(a,b)

print(a)
print(b)
print(c)
print(d)
