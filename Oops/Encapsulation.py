'''class Base:
    def __init__(self):
        self.p="javatipoint"
        self.q="java"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self.q)

o=Derived()
print(o.p)'''

class Car:
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))
    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()