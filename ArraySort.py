ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print("before sorting:")
print(ar)
print("after sorting: ")
for i in range(n):
    for j in range(i+1,n):
        if ar[i]>=ar[j]:
            temp=ar[i]
            ar[i]=ar[j]
            ar[j]=temp
print(ar)

