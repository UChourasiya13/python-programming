
x = lambda a,b,c : a+b+c
print(x(1,2,3))

print("======================================")

def myfun(n):
    return lambda a:a**n
mypow = myfun(2)
print(mypow(11))    