num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"Before swapping value of num1 is :{num1} and num2 is: {num2}")
temp = num1
num1 = num2
num2 = temp
print(f"after swapping value of num1 is :{num1} and num2 is: {num2}")

print("OR")

a = int(input("enter first number"))
b = int(input("enter first number"))
print("value before swapping")
print("a=" + str(a))
print("b=" + str(b))

temp = a
a  = b
b = temp
print("value after swapping")
print("a="+str(a))
print("b="+str(b))

