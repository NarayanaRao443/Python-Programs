n=int(input("Enter the number1: "))
sum=0
count=0
while n!=0:
    rem=n%10
    sum=sum+rem
    count=count+1
    n=n//10
print(sum)
print(count)