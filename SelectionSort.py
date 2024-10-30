ar=[4,2,5,1,0,9,6]
print(ar)

for i in range(0,len(ar)-1):
    min=i
    for j in range(i,len(ar)):
        if ar[j]<ar[min]:
            min=j 
    temp=ar[i]
    ar[i]=ar[min]
    ar[min]=temp
print(ar)


