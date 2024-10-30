n=int(input("Enter a number: "))
flag=False

if n==0 or n==1:
    flag=True
else:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break

if flag:
    print("not pirme")
else:
    print("prime")


