print("          LET'S DO SOME ARITHMATIC OPERATION USING MY CALCULATOR!!")

print("         SELECT CHOICE 1  FOR INTEGER INPUT AND CHOICE 2 FOR FLOATING INPUT")
choice= input("ENTER YOUR CHOICE: ")

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
5. modulus:\n"))

def Add(ranga , billa):
    return (ranga+billa)
def Sub(ranga , billa):
    return (ranga-billa)
def Mul(ranga , billa):
    return (ranga*billa)
def Div(ranga , billa):
    return (ranga/billa)
def Mod(ranga , billa):
    return (ranga%billa)

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
    print("The Division of ", NUM_1 ,"and",NUM_2,"is: ")
    print(Div(NUM_1 , NUM_2))
elif (operation==5):
    print("The Modulus of ", NUM_1 ,"and",NUM_2,"is: ")
    print(Mod(NUM_1 , NUM_2))   
else:
    print("OPERATION IS INVALID")
    
        
    








                 
    
      





