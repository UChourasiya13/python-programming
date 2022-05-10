str1 = "i am fine"
x = len(str1)
print("the length of string is:"+str(x))
print("the length of string is:{}".format(x))
print("the length of string is:",x)
for i in range(x):
    print(str1[i])
for i in range(x):
    print("{} is at index {}".format(str1[i] ,i))
for i in str1:
    print(str1.index(i))
    
for i in range(x-1,-1,-1):
    print(str1[i])
  
