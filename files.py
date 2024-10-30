# ----------read-----------
'''
f=open("example",'r')
#print(f.read())
print(f.readline(),end="")
#print(f.readline()) # prints one line only
#print(f.readlines(),end="") #prints whole string in list
#print(f.readline(4)) # returns 4 characters only
'''
'''
# --------write-------------
f=open('example2','w')
f.write('something')
f.write('good morning')

# --------append---------
f=open('example','a')
f.write('laptop')


f=open('example','r')
f1=open('example2','w')
for i in f:
    f1.write(i)
'''

#-------delete------------  
import os
if os.path.exists('hello'):
    os.remove('hello')
    print("file removed")
else:
    print("file does not exist")








