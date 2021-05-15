# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=Person("john","cina")
x.printname()

class Student(Person):
    pass
y=Student("Mike","olsen")
y.printname()
# class Principal(Student):
#     def __init__(self,fname,lname):
#         Student.__init__(self,fname,lname)
# z=Principal("david","hussey")
# z.printname()
# super keyword
class Principal(Student):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.addmission=year
        self.graduation=2022

z=Principal("david","hussey","2018")
z.printname()
print("addmision "+z.addmission ," gradution ",z.graduation)

