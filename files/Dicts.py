'''
d = {}
print(d)
print(type(d))

d = dict()
print(d)
print(type(d))

d[100] = "durga"
d[200] = "kalyan"
d[300] = "suresh"
print(d)

# Accessing data
d = {100:'Abc',200:'Def',300:'Ghi'}
print(d[100])
print(d[200])
print(d[300])

if 100 in d:
    print(d[100])


# update()
d = {100:'Abc',200:'Def',300:'efg'}
print(d)
d[100] = 'raju'
print(d)

d[400]='pavan'
print(d)

d[200]='sunnny'
print(d)

# Delete()
d = {100:'Abc',200:'Def',300:'Ghi'}
print(d)

del d[100]
print(d)

#del d[400] # key error
#print(d)

# clear()
d.clear()
print(d)

# Total dicitionary delete
# del d
del d
print(d) #name erro: d is not defined

#functions of dicionary
# 1. dict()

d = dict()
print(d)
d[100]='Abc'
d[200]= 'Dec'
print(d)

# 2. len()
print(len(d))

# 3. clear()
#d.clear()
#print(d)

# 4. get()
g = d.get(100)
print(g)

g = d.get(200,"guest") # here 200 exists in dictionary so it prints 200's value
print(g)

h = d.get(400,"Guest") # here 400 not exists in dictionary so it prints 'Guest' value
print(h)

# 5. pop()
d ={100:'abc',200:'def',300:'jgj',400:'kij',500:'hif'}
print(d)

# 6. popitem()
#print(d.pop(100))
d ={100:'abc',200:'def',300:'jgj',400:'kij',500:'hif'}
print(d.popitem())
print(d)
print(d.popitem())

e = {}
print(e.popitem()) # KeyError-> dictionary is empty


# 7. keys()
d ={100:'abc',200:'def',300:'jgj',400:'kij',500:'hif'}
print(d.keys())
for k in d.keys():
    print(k)

# 8. values()
print(d.values())
for j in d.values():
    print(j)


# 9. items()
d ={100:'abc',200:'def',300:'jgj',400:'kij',500:'hif'}
for k,v in d.items():
    print(k,"---",v)

# 10. copy()
d ={100:'abc',200:'def',300:'jgj',400:'kij',500:'hif'}
print(d)
d1 = d.copy()
print(d1)

# 11. setdefault()
d ={100:'abc',200:'def',300:'jgj',400:'kij',500:'hif'}
print(d)
print(d.setdefault(600,"pavan"))
print(d)

print(d.setdefault(100,"sachin")) # 100 :'abc' value is not replaced with sachin
print(d)
'''

# 12. update()
x={10:'z',20:'b',30:'w'}
print(x)
d ={100:'abc',200:'def',300:'jgj',400:'kij',500:'hif'}
d.update(x)
print(d)