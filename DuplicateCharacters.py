'''ar=input("Enter the string: ")
for i in range(0,len(ar)):
    count=1
    for j in range(i+1,len(ar)):
        if (ar[i]==ar[j] and ar[i]!=' '):
            count=count+1
            ar=ar[:j] + '0' +ar[j+1:]
    if count>1 and ar[i]!='0':
        print(ar[i],"-",count)

'''

ar=input("Enter the string:")
for i in range(len(ar)):
    count=1
    for j in range(i+1,len(ar)):
        if ar[i]==ar[j] and ar[i]!=' ':
            count=count+1
            ar=ar[:j]+'0'+ar[j+1:]
    if count>1 and ar[i]!='0':
        print(ar[i],'=',count)