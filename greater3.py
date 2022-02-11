#take 3 user defined integer and determine which number is greater
a = int(input("enter number a"))
b = int(input("enter number b"))
c = int(input("enter number c"))
if a>b and a>c:
    print(a,"is a greater than",b ,"and",c)
elif b>a and b>c:
    print(b,"is a greater than",a ,"and",c)
else:
    print(c," is a greater than",a ,"and",b)

    
