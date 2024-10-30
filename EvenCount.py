n=int(input("Enter the size of the array: "))
ar=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)

evenCount=0
oddCount=0
for i in range(len(ar)):
    if ar[i]%2==0:
        evenCount+=1
    else:
        oddCount+=1
print("EvenCount: ",evenCount)
print("OddCount: ",oddCount)

