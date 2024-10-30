'''list = []
print(list)
print(type(list))


s = "durga"
l =list(s)
print(l)

# split()
s = "Learning python is easy"
l  = s.split()
print(l)
print(type(l))

# Accessing the elements
l = [10,20,30,40]
print(l[1])
print(l[-1])


# slice
l = [1,2,3,4,5,6]
print(l)
print(l[1:4])
print(l[:3])
print(l[:-2])
print(l[1:5:2])


# indexing
n = [1,2,3,4,5,6]
n[2] = 10
print(n)
print(n.index(4))

# Functions of list
# len()
n  = [1,2,3,4,3,2,2,5]
print(len(n))
print(n.count(2))
print(n.count(5))
print(n.index(3))

# append()
n = [1,2,3,4,5,6,7]
print(n)
n.append(10)
print(n)

# insert
n = [10,20,30,'A','B']
print(n)
n.insert(1,100)
print(n)
n.insert(3,'Z')
print(n)

# extend()
n1 = ['A','B','C']
n2 = [10,20,30,'H','K']
n1.extend(n2)
print(n1)

# remove()
n = [1,2,3,4,'H','J','K']
print(n)
n.remove(3)
print(n)
n.remove('J')
print(n)

# pop()
n = [1,2,3,4,'J','K','A']
print(n)
n.pop()
print(n)
n.pop()
print(n)

n = []
n.pop()
print(n)

# Ordering 
# reverse()
n = [1,2,3,4,'a','b','c']
print(n)
n.reverse()
print(n)

# sort()
n = [4,2,4,1,5,7,0,6]
n.sort()
print(n)

# Mathematical Operations
# Concatenation
n = [1,2,3,'A','f','k']
k = [4,5,6,'l','M','R']
print(n+k)

# repetition
n = [1,2,3,'A','B','C']
print(n*3)

# Comparing List Objects
x = ["Dog","Rat","Cat"]
y = ["Dog","Rat","Cat"]
z = ["DOG","CAT","RAT"]

print(x==y) #True
print(x==z) #False
print(x!=z) #True


x = ["Dog","Cat","Rat"]
y = ["Rat","Cat","Dog"]
print(x==y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

x = [50,20,30]
y = [10,50,60,30,20]
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# Membership operator (in or not in)
n = [1,2,3]
print(1 in n)
print(10 in n)
print(10 not in n)
print(2 not in n)

# clear()
n = [1,2,3,4,5]
print(n)
n.clear()
print(n)
'''

# nested list
n = [1,2,3,[5,6],'A','B']
print(n)
print(n[0])
print(n[3])
print(n[3][0])
print(n[3][1])
print(n[4])