#filehandling

def fact(x):
        fact = 1
        if x==1 and x==0:
            return 1
        else:
            for i in range(1,x+1):
                fact = fact*i
            return fact


user_input = 5
y = fact(user_input)
print(user_input , y )
f= open("sample.txt" ,"w")
for i in range (5,21):
    #f.write("###########")
    z= "factorial of" + str(i)+ "is" + str(y)
    f.write(z)
    f.write("\n")
    #f.write("++++++++++++++++++++")




f= open("sample.txt" ,"r")
data1 = f.read()
print("this is the read operation")
print(data1)
dataline = data1.split("\n")
print(dataline)
dataline.pop()
print(dataline)
f.close()
    



    
