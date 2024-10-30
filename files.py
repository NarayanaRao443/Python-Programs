#f=open('abc2.txt','w')
#f=open('abc2.txt','a')
#f.write('hello\n')
#f.write('hi\n')
#f.write('good\n')

f=open('abc2.txt','r')
#print(f.read())

print(f.readline())
print(f.readline())
print(f.tell())

'''f=open('abc2.txt','w')
list = ['hyd\n','viz\n','bza\n','gunt\n','praka\n']
f.writelines(list)
'''