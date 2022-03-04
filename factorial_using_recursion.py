#factorial using recursion

def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        y = x*fact(x-1)
        return y

val =int(input("Enter a value: "))
func_val = fact(val)
print(f" factorial of {val} is {func_val}")          
          
