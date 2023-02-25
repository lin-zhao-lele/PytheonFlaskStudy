import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

## 创建一个表 - STAFF
# conn.execute('''CREATE TABLE STAFF
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print("Table created successfully");

## 插入数据
# conn.execute("INSERT INTO STAFF (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Maxsu', 27, 'Haikou', 20000.00 )");
#
# conn.execute("INSERT INTO STAFF (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 26, 'Shenzhen', 35000.00 )");
#
# conn.execute("INSERT INTO STAFF (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Weiwang', 23, 'Guangzhou', 22000.00 )");
#
# conn.execute("INSERT INTO STAFF (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Marklee', 25, 'Beijing', 45000.00 )");
# print ("Select Operation done successfully.");
# conn.commit()


cursor = conn.execute("SELECT id, name, address, salary  from STAFF")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")


print("Records Insert successfully");

conn.close()
