# list = [1,2,3,4,5,6,7]
# print(list[0])
# print(list[1])

# print(list[0:6])
# print(list[2:5])

# print(list[:])
# print(list[2:4])

# print(list[1:6:2])

# list = [1,2,3,4,5,6,7]
# print(list[-1])
# print(list[:-1])

# print(list[-3:])

# print(list[-3:-1])


# list = [1,2,3,4,5,6]
# print(list)

# list[5]=10
# print(list)

# list[1:3] = [40,50]
# print(list)

# list[-1] = 100
# print(list)


# Repetetion
'''
list = [1,2,3,4,5,6]
print(list)
print(list*2) #[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

# Concatenation
l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10,11,12]

print(l1+l2)  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Length
print(len(l1))

# Iteration
list = [10,20,30,40,50,60]
for i in list:
    print(i)

# Membership -> element exists or not

list2 = [10,20,30,40,50,60]
print(40 in list2) # True; 40 is exists in list2
print(100 in list2) # False; 100 is not exist in list2


list = ["John","Paul","Google","Amazon","Paytm"]
for i in list:
    print(i)

list.append("hello")
print(list)

'''

# Appending to the list
'''
li = []

n = int(input("Enter the size of the list: "))
for i in range(0,n):
    j = int(input("Enter a num: "))
    li.append(j)
    print(li[i])

print("list items are")
for i in li:
    print(i)

'''

# Removing element
'''
li = [4,22,5,12,9]
print("Original list")
for i in li:
    print(i)

li.remove(5) # 5 is remove from list

print("After removing element new list is:")
print(li)

'''
'''
list = [10,20,30,40,50]
print(list)

print(len(list))
print(max(list))
print(min(list))
'''

#Duplicate elements

list = [10,20,40,30,20,50,30,60,40,70]
list2 = []

for i in list:
   if i not in list2:
      list2.append(i)
           
print(list2)