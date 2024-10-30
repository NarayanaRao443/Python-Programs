'''ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x = int(input("Enter the elements of the array: "))
    ar.append(x)
print(ar)

def slarge(ar):
    fmax = ar[0]
    smax = ar[0]

    for i in range(1,len(ar)):
        if ar[i]>fmax:
            smax = fmax;
            fmax = ar[i]
        elif ar[i]>smax:
            smax = ar[i]
    #return (fmax,smax)
    return smax
print("Second largest element of the array is: ")      
sm = slarge(ar)
print(sm)'''


ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print(ar)

fmax = ar[0]
smax = ar[0]

for i in range(n):
    if ar[i]>fmax:
        smax=fmax
        fmax=ar[i]
    elif ar[i]>smax:
        smax=ar[i]
print("fmax: ",fmax)
print("smax: ",smax)
