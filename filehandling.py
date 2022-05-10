#filehandling

f=open("myfirstfile.txt","w")
x="ujjawal"
f.write(x)
y="chourasiya"
f.write("\n" + y)
f.close()

f=open("myfirstfile.txt","r")
y=f.read()
print(y)
f.close()

