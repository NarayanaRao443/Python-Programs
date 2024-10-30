'''import mysql.connector

#host='localhost' or host='127.0.0.1'

mydb = mysql.connector.connect(host='localhost',user='root',password='knr443',database='school')

mycursor = mydb.cursor()

mycursor.execute('select * from documents')

myres = mycursor.fetchall()

for x in myres:
    print(x)

mydb.close()

'''
'''from mysql.connector import (connection)

mydb = connection.MySQLConnection(user='root',password='knr443',host='localhost',database='school')

cursor = mydb.cursor()

cursor.execute('select *from faculty')
myres = cursor.fetchall()
for i in myres:
    print(i)

mydb.close()
'''

'''
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='knr443',database='school')
cursor = mydb.cursor()'''
#cursor.execute('create table tenth(sid int(10),sname varchar(20),smarks int(10))')
#print('table created')

'''sql = "insert into tenth(sid,sname,smarks) values(%s,%s,%s)"
rec = [(101,'sachin',200),(102,'dhoni',300),(103,'kohli',300)]

cursor.executemany(sql,rec)
mydb.commit()
print('values inserted')
'''
'''cursor.execute('select * from tenth')
myres = cursor.fetchall()

for i in myres:
    print(i)

mydb.close()'''


import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='knr443',database='school')

cursor = mydb.cursor()
#cursor.execute('create table inter (id int(10) primary key,name varchar(20),marks int(10))')
#print('table created')

#sql = "insert into inter (id,name,marks) values (%s,%s,%s)"
#rec = [(101,'raju',100),(102,'naveen',200),(103,'kumar',300)]

#cursor.executemany(sql,rec)
mydb.commit()
print('values inserted')

cursor.execute('select *from inter')
myres = cursor.fetchall()

for i in myres:
    print(i)

mydb.close()