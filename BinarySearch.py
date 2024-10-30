'''ar=[]
n = int(input("Enter the size of the array: "))
for i in range(n):
    x = int(input("Enter the elements of the array: "))
    ar.append(x)
print(ar)


key = int(input("Enter the key: "))
def binarySearch(ar,key):
    low = 0
    high = len(ar)-1

    while low<=high:
        mid = (low+high)//2

        if key < ar[mid]:
            high = mid-1
        elif key > ar[mid]:
            low = mid+1
        else:
            return True
    return False

if binarySearch(ar,key):
    print("Key is found")
else:
    print("Key is not found")

'''

'''ar=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    x=int(input("Enter the elements of the array: "))
    ar.append(x)
print(ar)

key = int(input("Enter the element to search: "))
low=0
high=len(ar)-1

while low<=high:
    mid=(low+high)//2
    if key<ar[mid]:
        high=mid-1
    elif key>ar[mid]:
        low=mid+1
    elif key==ar[mid]:
        print("key is found at ",mid)
        break
if low>high:
    print("Element is not found")
    '''

ar=[]
n=int(input("enter the size:"))
for i in range(n):
    x=int(input("enter the element:"))
    ar.append(x)
print(ar)

key=int(input("enter the key element: "))

low = 0
high = len(ar)-1

while low<=high:
    mid =(low+high)//2

    if key<ar[mid]:
        high=mid-1
    elif key>ar[mid]:
        low=mid+1
    elif key==ar[mid]:
        print("key found at",mid)
        break
if low>high:
    print("key is not found")