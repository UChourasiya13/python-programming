class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("----------------------")
        print("name is:", self.name)
        print("age is: ", self.age)
        print("----------------------")

class student(person):
    #pass
    def __init__(self,name , age ,gradyear):
        super().__init__(name,age)
        self.gradyear = gradyear

    def showDetails(self):
        print(self.name , self.age , self.gradyear)    


p1 = student("ujjawal", 18,2025)
p1.showDetails()
