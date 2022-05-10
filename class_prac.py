class person():
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def show(self):
        print("----------------------")
        print("name is:", self.name )
        print("age is: ",self.age)
        print("----------------------")


p1 = person("ujjawal" , 18)
p2 = person("tisha", 19)
p1.age = 19
#del p1.age
#print(p1.age)
#del p1
p1.show()
p2.show()
