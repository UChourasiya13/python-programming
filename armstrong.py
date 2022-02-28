#WAP for armstrong number!

num = int(input("Enter  a number: "))
temp = num
sum=0
while temp>0:
    r=temp%10
    sum+=r*r*r
    temp=temp//10
if (sum==num):
    print(num,"is a armstrong number")
else:
    print(num,"is not armstrong number")
    
