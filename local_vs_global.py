#local variable vs global variable

def user_input():
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    return (a,b)
def add(a,b):
    return(a+b)

a,b=user_input()
add(a,b)
print(a,"+",b,'=',add(a,b))    

