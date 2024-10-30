n=int(input("Enter the size of the array: "))
ar=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print(ar)

print(ar[::-1])


