print("-----LET'S DO SOME ARITHMATIC OPERATION USING MY CALCULATOR!!-----")

print("----------ENTER CHOICE 1  FOR INTEGER INPUT AND CHOICE 2 FOR FLOATING INPUT----------")
choice= input("ENTER YOUR CHOICE: ").lower()
op_type =input("ENTER TYPE OF OPERATION FOR TO BE PERFORMED i.e UNARY AND BINARY ").lower()

if op_type=="unary":
    if choice==('choice1'):
        NUM_1 = int(input("ENTER NUMBER: "))
    elif choice==('choice2'):
        NUM_1 = float(input("ENTER  NUMBER: "))
    else:
        print("ENTERED CHOICE IS DIFFERENT THAN RECOMENDED!")

    print("        SELECT UNARY OPERATION THAT IS TO BE PERFORMED: ")
    operation = int(input("1. square  \n\
2. square root \n\
3. cube\n\
4. cube root:\n"))
   

    def sq(x):
        return (x*x)
    def sqroot(x):
        y=x**(0.5)
        return (y)
    def cube(x):
        return (x**3)
    def cubeRoot(x):
        return (x**0.33)

    if (operation==1):
        print("The square of ", NUM_1 ,"is:")
        print(sq(NUM_1))
    elif (operation==2):
        print("The square root of ", NUM_1 ,"is: ")
        print(sqroot(NUM_1))
    elif (operation==3):
        print("The cube of ", NUM_1 ,"is: ")
        print(cube(NUM_1))   
    elif (operation==4):
        print("The cuberoot of ", NUM_1,"is: ")
        print(cubeRoot(NUM_1))
    else:
        print("OPERATION IS INVALID")    
    
        

    
    
    
    

elif op_type=="binary":
    if choice==('choice1'):
        NUM_1 = int(input("ENTER FIRST NUMBER: "))
        NUM_2 = int(input("ENTER SECOND NUMBER: "))
    elif choice==('choice2'):
        NUM_1 = float(input("ENTER FIRST NUMBER: "))
        NUM_2 = float(input("ENTER SECOND NUMBER: "))
    else:
        print("ENTERED CHOICE IS DIFFERENT THAN RECOMENDED!")

    print("        SELECT ARITHMATIC OPERATION THAT IS TO BE PERFORMED: ")
    operation = int(input("1. addition \n\
    2. substraction \n\
    3. multiplication\n\
    4. division\n\
    5. modulus:\n\
    6. power:\n"))

    def Add(x , y):
        return (x+y)
    def Sub(x , y):
        return (x-y)
    def Mul(x , y):
        return (x*y)
    def Div(x , y):
        return (x/y)
    def Mod(x , y):
        return (x%y)
    def power(x , y):
        return (x**y)

    if (operation==1):
        print("The Addition of ", NUM_1 ,"and",NUM_2,"is: ")
        print(Add(NUM_1 , NUM_2))
    elif (operation==2):
        print("The Substraction of ", NUM_1 ,"and",NUM_2,"is: ")
        print(Sub(NUM_1 , NUM_2))
    elif (operation==3):
        print("The Multiplication of ", NUM_1 ,"and",NUM_2,"is: ")
        print(Mul(NUM_1 , NUM_2))   
    elif (operation==4):
        if NUM_2==0:
            print("NUMBER IS DIVIDED BY ZERO")
        else:    
            print("The Division of ", NUM_1 ,"and",NUM_2,"is: ")
            print(Div(NUM_1 , NUM_2))
    elif (operation==5):
        print("The Modulus of ", NUM_1 ,"and",NUM_2,"is: ")
        print(Mod(NUM_1 , NUM_2))
    elif (operation==6):
        print("The Power of ", NUM_1 ,"and",NUM_2,"is: ")
        print(power(NUM_1 , NUM_2))
        
    else:
        print("OPERATION IS INVALID")
    
    
        
    








                 
    
      





