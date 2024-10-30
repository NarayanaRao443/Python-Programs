'''n=int(input("Enter the number:"))
fact=1
if n<0:
    print("factorial does not exist")
elif n==0:
    print(fact)
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)'''

n=int(input("enter number:"))
f=1
for i in range(1,n+1):
   f=f*i
print(f)