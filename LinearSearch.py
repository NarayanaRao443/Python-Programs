pos=-1
def linear(ar,key):
    for i in range(0,len(ar)):
        if ar[i]==key:
           globals() ['pos']=i
           return True
    return False

n=int(input("Enter the size of the array: "))
ar=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    ar.append(x)
print(ar)

key = int(input("Enter element to search: "))

if linear(ar,key):
    print("found at ",pos)
else:
    print("not found")


'''
pos=-1
def linear(ar,key):
    for i in range(0,len(ar)):
        if ar[i]==key:
           globals() ['pos']=i
           return True
    return False

ar=[1,2,3,4,5]
print(ar)
key = int(input("Enter element to search: "))

if linear(ar,key):
    print("found at ",pos)
else:
    print("not found")

'''


