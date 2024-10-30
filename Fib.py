'''n=int(input("Enter the number: "))
f1=0
f2=1
print(f1,f2,end=' ')
for i in range(n-2):
    f3=f1+f2
    print(f3,end=' ')
    f1=f2
    f2=f3'''

n=int(input("enter the number"))
f1=0
f2=1
print(f1,f2,end=' ')
for i in range(n-2):
    f3=f1+f2
    print(f3,end=' ')
    f1=f2
    f2=f3