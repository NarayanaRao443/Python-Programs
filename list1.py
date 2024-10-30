'''
l=[]
n = int(input("Enter the number of elements:"))
for i in range(0,n):
    l.append(input("Enter number:"))
print("Printing the list is:")
for i in l:
    print(i,end = " ")
'''
'''
l2 = [1,2,3,4,6]
print("Original list:")
for i in l2:
    print(i,end=" ")
    print("\n")
print("List Length\n")
print(len(l2))
print("Max element\n")
print(max(l2))
print("Min element\n")
print(min(l2))
l2.remove(3)
print("Updated list")
for i in l2:
    print(i,end=" ")
'''
'''
# Remove the duplicate elements from the list

l1 = [1,2,2,3,3,4,67,56,89,56,90]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# Sum of the elements of a list
s1 = [1,2,3,4,5,6]
sum=0
for i in s1:
    sum+=i
print("The sum is:",sum)

# find the common element in two lists

k1 = [1,2,3,4,5,6,7]
k2 = [8,9,10,3,2,11]
for i in k1:
    for j in k2:
        if i==j:
            print("Common elements:",i)

# Turn every item of a list into its square

n1=[1,2,3,4,5,6]
res=[]
for i in n1:
    res.append(i*i*i)
print(res)
'''
# sum of list
l1=[1,2,3,4,5]
sum = 0
for i in l1:
    sum = sum+i
print(sum)

# Multiplication of list
l1=[1,2,3,4,5]
sum = 1
for i in l1:
    sum = sum*i
print(sum)

# Largest from the list
l1=[1,2,31,4,5]
max = l1[0]
for i in l1:
    if i > max:
        max = i
print(max)

# smallest from the list
l1 = [11,12,-1,14,5]
min = l1[0]
for i in l1:
    if i < min:
        min = i
print(min)
