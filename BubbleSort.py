'''n=int(input("Enter the size of the array: "))
ar=[]
for i in range(n):
    x=int(input("Enter the element: "))
    ar.append(x)
print(ar)

print("After sorting: ")
for i in range(n-1):
    for j in range(n-i-1):
        if ar[j]>ar[j+1]:
            temp=ar[j]
            ar[j]=ar[j+1]
            ar[j+1]=temp
print(ar)
'''

# descending order
n=int(input("Enter the size of the array: "))
ar=[]
for i in range(n):
    x=int(input("Enter the element: "))
    ar.append(x)
print(ar)

for i in range(n-1):
    for j in range(n-i-1):
        if ar[j]<ar[j+1]:
            t=ar[j]
            ar[j]=ar[j+1]
            ar[j+1]=t
print(ar)