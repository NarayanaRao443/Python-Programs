class A:
    def add(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s
s1 = A()
print(s1.add(10,20))
print(s1.add(10,20,30))
print(s1.add(10))


