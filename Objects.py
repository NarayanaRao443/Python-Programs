class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("My name is ",self.name ," and my age is ",self.age)
p=Person('raj',40)
p.func()