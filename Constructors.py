'''
class A:
    def __init__(self):
        print("A class")
    def feature1(self):
        print("feature 1 class")
class B:
    def __init__(self):
        print("B class")
    def feature2(self):
        print("feature 2 class")
a=A()
a.feature1()
b=B()
b.feature2()     
'''



'''
class A:
    def __init__(self):
        print("A class")
    def feature1(self):
        print("feature 1 class")
class B(A):
    def __init__(self):
        super().__init__()
        print("B class")
    def feature2(self):
        print("feature 2 class")

a=A()
a.feature1()

b=B()
b.feature1()
b.feature2()
'''


# Method Resolution Order(MRO)
# Method calls from the left to right side by class;
# here super() takes the methods from the left to right side in class declaration
# ex: C(A,B) here A will calls first, B class won't executed
# ex: C(B,A) here B will calls first, A class won't executed

class A:
    def __init__(self):
        print("A class")
    def feature1(self):
        print("feature 1A class")
    def feature2(self):
        print("feature 2A class")
class B:
    def __init__(self):
        print("B class")
    def feature1(self):
        print("Feature 1B class")
    def feature2(self):
        print("feature 2B class")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("C class")

    def feat(self):
        super().feature2()

a=C()
a.feature1()
a.feat()

