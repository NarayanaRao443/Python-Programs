'''
s = {10,20,30,40}
print(s)
print(type(s))

s = {} # set acts like dictionary but not accepts the key-value pairs
print(type(s))

s = set()
print(s)
print(type(s))

s = {10,20,40,20,40,50,30,20,10}
print(len(s))
print(s)

s = set(range(5))
print(s)

# functions of set
# 1. add(x)
s = {10,20,30}
s.add(40)
s.add(50)
print(s)

# 2. update(x,y,z)
s = {10,20,30,40}
l = {10,40,50,60}
s.update(l,range(6))
print(s)

s = {11,12,13}
l = {8,9,10}
s.add(4) # valid to add elements to set
print(s)

#s.add(10,20,30) # invalid to add elements to set
#print(s)

#s.update(10) # invalid to update elements of set
#print(s)

s.update(l,range(5))
print(s)

# 4. copy()
s= {1,2,3}
s1 = s.copy()
print(s)
print(s1)

# 5. pop() # pop the random element

s = {100,10,30,20,20,10}
print(s)
print(s.pop())
print(s)
print(s.pop())

# 6. remove(x)

s = {1,2,3,4,5,5,6}
print(s)
s.remove(5)
print(s)
s.remove(50) # key error; 50 is not in set
print(s)

# 7. discard
s = {10,20,30}
s.discard(10)
print(s)
s.discard(50)
print(s)

# 8. clear()
s = {10,20,30,40}
s.clear()
print(s) # set()

# Mathematical operations
# 1. Union()
x = {10,20,30}
y = {40,50,60}
#print(x.union(y))
print(x|y)

# 2. intersection()
x = {10,20,30,40}
y = {20,30,40,50,60}
print(x.intersection(y))
print(x&y)

# 3. difference
x = {10,20,30,40,80}
y = {20,30,40,50,60,70}
print(x.difference(y))
print(x-y)
print(y.difference(x))
print(y-x)

# 4. symmetric difference
x = {10,20,30,40}
y = {30,40,50,60}
print(x.symmetric_difference(y))
print(x^y)

# Membership operator(in or not in)
s = {10,20,30,40}
print(s)
print(10 in s) # True
print(10 not in s) # False
print(100 not in s) # True
print(100 in s) # False

s  = {"durga"}
print(s)
s = set("durga")
print(s)
print('d' in s ) # True
print('d' not in s) # False
'''

s = {10,20,30,'A','d','c'}
print(s)