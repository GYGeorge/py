import random
import pandas as pd
import pymysql
con = pymysql.connect(host = 'localhost', user = 'root', port = 3306, password = '496532343', db = "curriculum")

cursor = con.cursor()

for i in range(1001,1000000):
    sno = str(i + 161700000)
    coursenum = random.randint(0,3)
    if coursenum != 0:
        cno1 =random.randint(1,30)        
        grades = random.randint(60,100)
        
        insertsql = "insert into sc values('%s','%s','%d')" % (sno, str(cno1), grades) 
        cursor.execute(insertsql)
        coursenum = coursenum - 1
    if coursenum != 0:
        cno2 = random.randint(31,60)
        grades = random.randint(60,100)
        
        insertsql = "insert into sc values('%s','%s','%d')" % (sno, str(cno2), grades) 
        cursor.execute(insertsql)
        coursenum = coursenum - 1
    if coursenum != 0:
        cno3 =random.randint(61,90)        
        grades = random.randint(60,100)
        
        insertsql = "insert into sc values('%s','%s','%d')" % (sno, str(cno3), grades) 
        cursor.execute(insertsql)
        coursenum = coursenum - 1
   
        
con.commit()
cursor.close()
con.close()