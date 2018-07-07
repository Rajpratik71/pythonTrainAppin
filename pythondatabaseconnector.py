import mysql.connector
db=mysql.connector.connect(host='localhost,database='appin',user='root',password='redhat',port='3307')
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTES EMPLOYEE')
sql="""CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT_NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAAR(1),INCOME FLOAT)"""
cursor.execute()(sql)
db.close()
