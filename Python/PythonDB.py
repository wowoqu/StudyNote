import pymysql
import MySQLdb
print(MySQLdb)

# conn = pymysql.connect(
#     host = '127.0.0.1',
#     port = 3306,
#     user = 'root',
#     passwd = '123456',
#     db = 'testpython',
#     charset = 'utf8'
# )

conn = pymysql.connect('localhost','root','123456','testpython')
#这两种方法都是可行的

cursor = conn.cursor()

conn1 = MySQLdb.connect('localhost','root','123456','testpython')
cursor1 = conn1.cursor()


sql = 'select * from test'
cursor1.execute(sql)

rs = cursor1.fetchall()
for row in rs:
	print('id=%d,title=%s,author=%s'%row)

# sql_insert = "INSERT INTO test(\
# 			    title,author)\
# 			    VALUES\
# 			    ('ABC','DEF')"
sql_insert = "insert into test(\
				title)\
				values\
				('abc')"


try:
	cursor1.execute(sql_insert)
	conn1.commit()
except Exception as e:
	print(e)
	conn1.rollback()



print(conn1)
print(cursor1)

cursor1.close()
conn1.close()
