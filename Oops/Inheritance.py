# single level inheritance
'''
class A:
    def feature1(self):
        print("feature 1A working")
    def feature2(self):
        print("feature 2A working")
class B(A):
    def feature3(self):
        print("feature 3B working")
    def feature4(self):
        print("feature 4B working")

a=A()
a.feature1()
a.feature2()
print()
b=B()
b.feature1()
b.feature3()
b.feature2()
b.feature4()
'''



# Multilevel inheritance
'''
class A:
    def feature1(self):
        print("feature 1A working")
    def feature2(self):
        print("feature 2A working")
class B(A):
    def feature3(self):
        print("feature 3B working")
    def feature4(self):
        print("feature 4B working")

class C(B):
    def feature5(self):
        print("feature 5c working ")
    def feature6(self):
        print("feature 6c working")

a=A()
a.feature1()
a.feature2()
print()
b=B()
b.feature1()
b.feature3()
b.feature2()
b.feature4()
print()

c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()
'''

# Heirarchical Inheritance

'''
class A:
    def feature1(self):
        print("feature 1A working")
    def feature2(self):
        print("feature 2A working")
class B(A):
    def feature3(self):
        print("feature 3B working")
    def feature4(self):
        print("feature 4B working")

class C(A):
    def feature5(self):
        print("feature 5c working ")
    def feature6(self):
        print("feature 6c working")
a=A()
a.feature1()
a.feature2()
print()

b=B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()
print()

c=C()
c.feature1()
c.feature2()
c.feature5()
c.feature6()
print()
'''


# Hybrid Inheritance
'''
class A:
    def feature1(self):
        print("feature 1A working")
    def feature2(self):
        print("feature 2A working")
class B(A):
    def feature3(self):
        print("feature 3B working")
    def feature4(self):
        print("feature 4B working")

class C(B):
    def feature5(self):
        print("feature 5c working ")
    def feature6(self):
        print("feature 6c working")
class D(B):
    def feature7(self):
        print("feature 7d working")
    def feature8(self):
        print("feature 8d working")

a=A()
a.feature1()
a.feature2()
print()

b=B()
b.feature1()
b.feature3()
b.feature2()
b.feature4()
print()

c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()
print()

d=D()
d.feature1()
d.feature2()
d.feature3()
d.feature4()
d.feature7()
d.feature8()'''


# Multiple Inheritance
'''
class A:
    def feature1(self):
        print("feature 1A working")
    def feature2(self):
        print("feature 2A working")
class B:
    def feature3(self):
        print("feature 3B working")
    def feature4(self):
        print("feature 4B working")
class C(A,B):
    def feature5(self):
        print("feature 5C working")
    def feature6(self):
        print("feature 6C working")

a=A()
a.feature1()
a.feature2()
print()

b=B()
b.feature3()
b.feature4()
print()

c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()
'''


class A:
    def f1(self):
        print('f1')
class B():
    def f2(self):
        print('f2')
class C(A,B):
    def f3(self):
        print('f3')
a=A()
a.f1()
print()

b=B()
b.f2()
print()

c=C()
c.f1()
c.f2()
c.f3()
print()
