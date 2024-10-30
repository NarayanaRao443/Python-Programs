n = int(input("Enter the size of the array: "))
ar=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print(ar)

pos=int(input("Enter the position to delete: "))
if pos>=n+1:
    print("deletion is not possible")
else:
    for i in range(pos-1,n-1):
        ar[i]=ar[i+1]
    for i in range(n-1):
        print(ar[i])   