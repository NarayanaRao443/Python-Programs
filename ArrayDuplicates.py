n=int(input("Enter the size of the array: "))
ar=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print(ar)

print("Duplicate elements are: ")
for i in range(n):
    for j in range(i+1,n):
        if ar[i]==ar[j]:
            print(ar[i])
            


