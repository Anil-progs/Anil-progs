#Chection of python with mysql
    #to handle mysql database from python you need to install three things
        #1 python
            #python --version
        #2 mysql
            #pip install mysql
        #3 mysql driver
            # pip install mysql.connetor-python

import mysql.connector
print("mysql is connected")
>>>mysql is connected

#Step 1:create connection
import mysql.connector as myconn
mydb=myconn.connect(
    host=="localhost",
    user="user name",
    password="password",
    database="database name")   # it is optional
print(mydb)

#step 2: create database
    mysql
    python (jain the front end with database we will do it with python language)

db_cursor=mydb.cursor()
db_cursor.execute('create database LearningCoding')

import mysql.connector as myconn
mydb=myconn.connect(
    host="Localhost",
    user="root",
    password="1998",   
)

db_cursor=mydb.cursor()
db_cursor.execute("create database LearnCoding")
print("LearnCoding database is create")
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
cmd coment
mysql -u root -p  (it will ask you your mysql password it is true it will inter)
\c (use for go back)   
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| learncoding        |
| library            |
| mysql              |
| performance_schema |
+--------------------+
5 rows in set (0.00 sec)

# Step 3: Create tables
db_cursor=mydb.cursor()               #you need to get the name of your database
db_cursor.execute('create table emp(name varchar(20),
roll number)')      
import mysql.connector as myconn
mydb=myconn.connect(
    host="Localhost",
    user="root",
    password="1998",
    database="LearnCoding"   #clear the database
)

db_cursor=mydb.cursor()
db_cursor.execute('create table emp(Roll int,Ename varchar(20))')
print("your table is create")

#it is for show the table
db_cursor=mydb.cursor()
db_cursor.execute('show tables')
for i in db_cursor:
    print(i)
#>>>('emp',)

db_cursor=mydb.cursor()
db_cursor.execute('create table emp2(Roll int, Ename varchar(20),jap varchar(40))')
print("you create the second table as will as")
#>>>you create the second table as will as
#PS C:\Users\MRC>


# it is for show the databse
db_cursor=mydb.cursor()
db_cursor.execute('show tables')
for i in db_cursor:
    print(i)
>>>('emp',)
('emp2',)



#Step 4: insert record
insert_query="insert into emp(name,Roll) values (%s,%s)"
insert_value("Ahmad",10)
db_cursor.execute(insert_query,insert_value)
mydb.commit()
>>>1 Record insert


import mysql.connector as myconn
mydb=myconn.connect(
    host="Localhost",
    user="root",
    password="1998",
    database="LearnCoding"   #clear the database
)

db_cursor=mydb.cursor()
db_insert="insert into emp(Roll,Ename) values (%s,%s)"
db_list=[(30,"ali"),(50,"hamad"),(60,"zaher")]
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print(db_cursor.rowcount,"Record insert")

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
cmd comment
>>>mysql>> select * from LearnCoding.emp;
+------+-------+
| Roll | Ename |
+------+-------+
|   10 | Ahmad |
+------+-------+

db_cursor=mydb.cursor()
db_cursor.execute('insert into emp(Roll,Ename) values(%s,%s)',(40,"Mohammad"))
mydb.commit()
print(db_cursor.rowcount,"Record insert")
>>>mysql>> select * from LearnCoding.emp;
+------+----------+
| Roll | Ename    |
+------+----------+
|   10 | Ahmad    |
|   40 | Mohammad |
+------+----------+
2 rows in set (0.00 sec)
#when we want to insert many of of datas
db_cursor=mydb.cursor()
db_insert="insert into emp(Roll,Ename) values (%s,%s)"
db_list=[(30,"ali"),(50,"hamad"),(60,"zaher")]
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print(db_cursor.rowcount,"Record insert")
>>>mysql> select * from  LearnCoding.emp;
+------+----------+
| Roll | Ename    |
+------+----------+
|   10 | Ahmad    |
|   40 | Mohammad |
|   30 | ali      |
|   50 | hamad    |
|   60 | zaher    |
+------+----------+
5 rows in set (0.00 sec)

#Step 5: Select record
db_cursor.execute('select * from emp')
myresult=db_cursor.fetchall()


import mysql.connector as myconn
mydb=myconn.connect(
    host="Localhost",
    user="root",
    password="1998",
    database="LearnCoding"   #clear the database
)

db_cursor=mydb.cursor()
db_cursor.execute('select * from LearnCoding.Emp')
data=db_cursor.fetchall()
print(data)
>>>[(10, 'Ahmad'), (40, 'Mohammad'), (30, 'ali'), (50, 'hamad'), (60, 'zaher')]
PS C:\Users\MRC> 

\\\\\\\\\\\\\\\\\\\\\\\\\\\\
db_cursor=mydb.cursor()
db_cursor.execute('select * from LearnCoding.Emp')
for data_cursor in db_cursor:
    print(data_cursor)
>>>
(10, 'Ahmad')
(40, 'Mohammad')
(30, 'ali')     
(50, 'hamad')   
(60, 'zaher')   
PS C:\Users\MRC> 


#Step 6: update record 
updata_query='update emp set Roll=%s where name =%s'
set_value=('50',anil)
db_cursor.execute(updata_query,set_value)


import mysql.connector as myconn
mydb=myconn.connect(
    host="Localhost",
    user="root",
    password="1998",
    database="LearnCoding"   #clear the database
)

db_cursor=mydb.cursor()
db_updatedata="update LearnCoding.emp set Roll=%s where Ename=%s"
db_value=(60,"zaher")
db_cursor.execute(db_updatedata,db_value)
mydb.commit()
print(db_cursor.rowcount,"it already update")
>>>0 it already update

cmd commad
>>>mysql> select * from LearnCoding.emp;
+------+----------+
| Roll | Ename    |
+------+----------+
|   10 | Ahmad    |
|   40 | Mohammad |
|   30 | ali      |
|   50 | hamad    |
|   60 | zaher    |
+------+----------+
5 rows in set (0.00 sec)


#Step 7: Delete record
delete_record='delete from emp where Roll=%s'
value=('10',)
db_cursor.execute(delete_record,value)
mydb.commit()


import mysql.connector as myconn
mydb=myconn.connect(
    host="Localhost",
    user="root",
    password="1998",
    database="LearnCoding"   #clear the database
)

db_cursor=mydb.cursor()
db_delete="delete from LearnCoding.emp where Ename=%s"
db_value=("zaher",)
db_cursor.execute(db_delete,db_value)
mydb.commit()
print(db_cursor.rowcount,"Record deleted")
>>>1 Record deleted
PS C:\Users\MRC> 
cmd commend

>>>mysql> select * from LearnCoding.emp;
+------+----------+
| Roll | Ename    |
+------+----------+
|   10 | Ahmad    |
|   40 | Mohammad |
|   30 | ali      |
|   50 | hamad    |
+------+----------+
4 rows in set (0.00 sec)

\\\\\\\\\\\\\\\\\\\\\\
# it will delete all of it
import mysql.connector as myconn
mydb=myconn.connect(
    host="Localhost",
    user="root",
    password="1998",
    database="LearnCoding"   #clear the database
)

db_cursor=mydb.cursor()
db_delete="truncate table LearnCoding.emp"
db_cursor.execute(db_delete)
mydb.commit()
print(db_cursor.rowcount,"Record deleted")
>>>0 Record deleted
PS C:\Users\MRC> 




