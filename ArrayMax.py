'''ar=[]
n = int(input("Enter the size of list: "))
for i in range(n):
    x = int(input("Enter the elements of the list: "))
    ar.append(x)
print(ar)

def largest(ar):
    maxi = ar[0]
    for i in range(1,len(ar)):
        if maxi < ar[i]:
            maxi = ar[i]
    return maxi 
print("Largest element of the array is: ")
m = largest(ar)
print(m)'''


ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x=int(input("Enter the elments: "))
    ar.append(x)
print(ar)

maxi = ar[0]
for i in range(n):
    if ar[i]>maxi:
        maxi=ar[i]
print('max element:',maxi)



