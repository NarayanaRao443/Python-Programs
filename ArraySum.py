ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print("Array is: ",ar)

sum=0
for i in range(n):
    sum=sum+ar[i]
print("array sum is: ",sum)