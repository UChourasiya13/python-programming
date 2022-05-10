#Arbitrary argument

def avg(*value):
    x = 0
    for i in value:
        x = x+i
    return x/len(value)
y = avg(3,4,5,2,3,3,4,4,5,3,2,3,2.4,2.4,1.222,1)
print(y)
