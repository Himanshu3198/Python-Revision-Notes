class MyClass:
    x=5
p1 =MyClass()
print(p1.x)
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
 
class Person:
    def __init__(self,name,age):
     self.name= name
     self.age=age
    
    def myfunc(abc):
        print("hello my name is " + abc.name)

p2=Person("john",24)
print(p2.name)
print(p2.age)
p2.myfunc()
# modify object properties
p2.name="rahul"
print(p2.name)
# delete object properties
del p2.age
print(p2.age)

