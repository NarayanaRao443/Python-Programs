import os,sys
fname = input("Enter the file name: ")
if os.path.isfile(fname):
    print("File exists",fname)
    f = open(fname,'r')
else:
    print("File not exist")
    sys.exit(0)

lcount = wcount = ccount = 0
for line in f:
    lcount+= 1
    ccount += len(line)
    words = line.split()
    wcount += len(words)
print("lcount: ",lcount)
print("ccount: ",ccount)
print('wcount: ',wcount)
f.close()