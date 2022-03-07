#LCM OF 2 NUMBER

num1,num2 = int(input("ENTER FIRST NUMBER FOR LCM: ")),int(input("ENTER SECOND NUMBER FOR LCM: "))
 
for i in range(1,num1 *num2 +1):
    if i%num1==0 and i%num2==0:
        print("LCM IS:",i)
        break
