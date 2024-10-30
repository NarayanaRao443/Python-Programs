class A:
    def show(self):
        print("A showing")
class B(A):
    def show(self):
        print("B showing")
a=B()
a.show()        