'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number: "))
fact = factorial(n)
print(fact)'''

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter number:"))
print(fact(n))
