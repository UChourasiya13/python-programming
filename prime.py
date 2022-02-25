#check a number it is prime or not
x = int(input("Enter a number : "))
y=2
while(y<=x-1):
    if(x%y==0): 
        print("number is not prime")
        break
    y=y+1
if(x==y):
    print("prime no")



    
