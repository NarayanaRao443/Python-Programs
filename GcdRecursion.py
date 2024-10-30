'''def gcd(n1,n2):
    if n2!=0:
        return gcd(n2,n1%n2)
    else:
        return n1
n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))

print(gcd(n1,n2))
'''

def gcd(n1,n2):
    if n2!=0:
        return gcd(n2,n1%n2)
    else:
        return n1
n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))

print(gcd(n1,n2))