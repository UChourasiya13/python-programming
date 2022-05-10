def fact(x):
    fact = 1
    if x==1 or x==0:
        return 1
    else:
        for i in range(1,x+1):
            y = fact*i 
        return 

user_input = 5
y = fact(user_input)
print(user_input,y)