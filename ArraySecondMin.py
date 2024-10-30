'''ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x = int(input("Enter the elements of the array: "))
    ar.append(x)
print(ar)

def smallest(ar):
    fmin = ar[0]
    smin = ar[0]

    for i in range(1,len(ar)):
        if ar[i]<fmin:
            smin = fmin;
            fmin = ar[i]
        elif ar[i]<smin:
            smin = ar[i]
    #return (fmin,smin)
    return smin
print("Second smallest element of the array is: ")      
sm = smallest(ar)
print(sm)'''


ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print(ar)

fmin = ar[0]
smin = ar[0]

for i in range(n):
    if ar[i]<fmin:
        smin=fmin
        fmin=ar[i]
    elif ar[i]<smin:
        smin=ar[i]
print("fmin: ",fmin)
print("smin: ",smin)