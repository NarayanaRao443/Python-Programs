ar=[3,2,4,2,1,5]
print(ar)
for i in range(len(ar)):
    key=ar[i]
    j=i-1
    while j>=0 and ar[j]>key:
        ar[j+1]=ar[j]
        j=j-1
    ar[j+1]=key
print(ar)



