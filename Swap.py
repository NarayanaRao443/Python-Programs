n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))

print("Before Swap")
print(n1)
print(n2)

'''temp=n1
n1=n2
n2=temp'''

n1=n1+n2
n2=n1-n2
n1=n1-n2

print("After Swap")
print(n1)
print(n2)