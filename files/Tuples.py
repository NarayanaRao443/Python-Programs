'''
t = (10,20,30,40)
print(t)
print(type(t))

t = ()
print(type(t))

t = (10)
print(type(t))  # int

t = ("b")
print(type(t))  # string

t = (10,)  # comma represents tuple; without comma it is only int
print(type(t))

t = ("B",)  # comma represents tuple; without comma it is only string
print(type(t))

# Tuple creation 
# paranthesis () are optional
t = 10,
print(t)
print(type(t))

k = (10,)
print(k)
print(type(k))

n = 10,20,30
print(n)
print(type(n))

k = (10,20,30)
print(k)
print(type(k))

# tuple() function
n = [10,20,30]
print(n)
t = tuple(n) # list converted to tuple
print(t)

# list() function
t = (10,20,40)
print(t)
n = list(t) # tuple converted to list
print(n)

# Accessing elements
# 1.By using index
t = (10,20,30,40,50)
print(t[0])
print(t[4])
print(t[-1])

# 2. slice operator
t = (10,20,30,40,50)
print(t[2:4])
print(t[2:100])
print(t[::2])
print(t[-3:-1])

# Mathematical operations
# 1. Concatenation
t1 = (10,20,40)
t2 = (40,50,60)
print(t1+t2)

# 2. Repetition / Multiplication
t1 = (10,20,30)
print(t1*2)


# Functions of Tuple
# 1. len()
t = (10,20,30,40,50)
print(t)
print(len(t))

# 2. count()
t = (10,20,30,40,50,20,30,20)
print(t.count(20))

# 3. index()
t = (10,20,30,20,40,50)
print(t.index(20))

# 4. sorted()
t = (4,2,0,5,1,3)
print(sorted(t))

# 5. min()
t = (4,2,1,4,6,7,0,)
print(min(t))

# 6. max()
t = (4,2,1,4,6,7,0,)
print(max(t))
'''

# Comaparison 
t1 = (10,20,30)
t2 = (40,50,60)
t3 = (10,20,30)
print(t1<t2)
print(t1>t2)
print(t1==t3)

