#WAP for to check wheather a number is palindrome or not

num = int(input("Enter  a number: "))
temp = num
sum=0
while temp>0:
    r=temp%10
    sum=sum*10 + r
    temp=temp//10
if (sum==num):
    print(num,"is a palindrome number")
else:
    print(num,"is not palindrome number")
