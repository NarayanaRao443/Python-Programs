n = int(input("Enter the number: "))
x=n
sum=0
while (n!=0):
    rem = n%10
    sum = sum+(rem**3)
    n = n//10

if sum==x:
    print("armstrong")
else:
    print("not armstrong")
