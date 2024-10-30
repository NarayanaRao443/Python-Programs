'''def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the number: "))
for i in range(n):
    print(fib(i),end=' ')
'''


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter a no: "))
for i in range(n):
    print(fib(i),end=' ')