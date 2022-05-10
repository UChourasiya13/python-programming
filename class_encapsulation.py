class person():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  #double underscore is used to declare private mem
class student(person):
    def __init__(self, name, age):
        person.__init__(self,name, age)
        print("calling private mem of base class", self.__age)
p1 = student("ujjawal" , 18)
p1.age