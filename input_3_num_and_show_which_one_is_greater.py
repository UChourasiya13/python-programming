#take 3 user defined integer and determine which number is greater
a = int(input("enter number a"))
b = int(input("enter number b"))
c = int(input("enter number c"))
if a==b==c:
    print("all are same")
elif a==b>c:
    print("a:",a ,"and","b:", b ,"are same and greater than ","c:",c)
elif a==c>b:
    print("a:",a ,"and", "c:",c ,"are same and greater than ","b:",b)
elif b==c>a:
    print("b",b,"and","c", c ,"are same and greater than ","a:",a)
elif a>b and a>c:
    print("a:",a,"is a greater than","b:",b ,"and","c:",c)
elif b>a and b>c:
    print(b,"is a greater than",a ,"and",c)
else:
    print(c," is a greater than",a ,"and",b)
