# 1) Write a python program to create a Student class and creates an object to it. Call the method talk() to display the student details
'''
class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("Hello ",self.name)
        print("RoolNo is ",self.rollno)
        print("Marks ",self.marks)

s = Student('Raju',130443,450)
s.talk()
'''

class Student:
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z 
    def display(self):
        print("Name: {}\n Rollno: {}\n Marks:{} ".format(self.name,self.rollno,self.marks))
    
s = Student("Durga",10,120)
s.display()