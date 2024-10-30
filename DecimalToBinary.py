n=int(input("Enter the decimal number: "))
bin=0
i=1
while n!=0:
    rem=n%2
    bin=bin+rem*i
    n=n//2
    i=i*10
print(bin)
'''
n=int(input("Enter the binary number: "))
dec=0
i=0
while n!=0:
    rem=n%10
    dec=dec+rem*pow(2,i)
    n=n//10
    i=i+1
print(dec)'''