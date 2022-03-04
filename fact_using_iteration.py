num = int(input("Enter a number for factorial: "))
temp = num
fact = 1
while(num>0):
    fact = fact*num
    num = num-1
print(f"factorial of {temp} is {fact}" )    
