'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person('raj',30)
print(p.name)
print(p.age)'''

#The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        
p = Person('raj',30)
print(p)

#The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
        
p = Person('raj',30) #object
print(p)
         