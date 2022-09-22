import mysql.connector as conn
mydb=conn.connect(host='localhost',user='root',passwd='Sql@jit1')
cursor=mydb.cursor()
# cursor.execute("create database if not exists review")
# cursor.execute("create table if not exists tasksql.mytable(name varchar(30),number int)")