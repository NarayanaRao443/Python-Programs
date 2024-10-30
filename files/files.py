# f = open('abc.txt','w')
# print("File Name: ",f.name)
# print("File Mode: ",f.mode)
# print("File Readable: ",f.readable())
# print("File Writable: ",f.writable())
# print("Is file closed:",f.closed)
# f.close()
# print("Is file closed: ",f.closed)

# We can writing the data into file by two ways
# write()
# writelines()
'''
# write()
# Write into file
f = open('abc.txt','w')
f.write("Durga\n")
f.write("Software\n")
f.write("Solutions\n")
f.close()

# append the data. previous data is not overridden
f = open('abc.txt','a')
f.write("hyderabad\n")
f.write("sr nagar\n")
f.write("kaamakshi")
f.close()

# writeline()

f = open('abcd.txt','w')
list = ['hyd\n','viz\n','bza\n','gunt\n','praka\n']
f.writelines(list)
f.close()


# 2. read()
f = open('abc.txt','r')
print(f.read())
f.close()

# read(n)
f = open('abc.txt','r')
print(f.read(8))
f.close()


# readline() 
# read data line by line

f = open('abc.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')
print(f.readline(),end='')
f.close()


# readlines()
# read all lines same time
f = open('abc.txt','r')
lines = f.readlines()
for i in lines:
    print(i,end='')
f.close()


f = open('abc.txt','r')
print(f.read(3))
print(f.readline())
print(f.read(4))
print("remaining data")
print(f.read())
f.close()


# tell() # tells about the cursor position in the file
f = open('abc.txt','r')
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(5))
print(f.tell())
f.close()
'''

# seek() # this method used to move the cursor from one pointer to sepcified location

'''
Durga
Software
Solutions
hyderabad
sr nagar
kaamakshi'''


data = "All Students are Stupids"
f = open('abc.txt','w')
f.write(data)
with open('abc.txt','r+') as f:
    text = f.read()
    print(text)

    print("Cursor current position: ",f.tell())
    f.seek(17)
    print("Cursor current position: ",f.tell())
    f.write('Gems!!!')
    f.seek(0)
    text = f.read()
    print("After data modification")
    print(text)
f.close()


