import mysql.connector
db = mysql.connector.connect(host='localhost',database='appin',user='root',password='',port='3306')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)"""
cursor.execute(sql)
db.close()
