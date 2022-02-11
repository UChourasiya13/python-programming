#write a code for odd and even number such that the number is inputed from user and if the number is zero then print its neither even nor odd
x = float(input("please enter a number"))
print(type(x))
value = x%2
print(value)
if x==0:
    print("x is neither even nor odd")
elif x%2==0:
    print("x is even number")
else:
    print("x is a odd number")
    
