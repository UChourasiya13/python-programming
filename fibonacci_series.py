#WAP for fibonacci series


num = int(input("Enter a number upto which you want fibonacci series : "))
a = 0
b = 1

while(a<num-1):
    c=a+b
    print(c)
    a=b
    b=c


    
