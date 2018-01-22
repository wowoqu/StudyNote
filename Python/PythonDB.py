import pymysql
# print(MySQLdb)

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

sql = 'select * from test'
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
	print('id=%d,title=%s,author=%s'%row)

sql_insert = "INSERT INTO test(\
			    title,author)\
			    VALUES\
			    ('ABC','DEF')"
sql_insert = "insert into test(\
				title,author)\
				values\
				('abc','def')"


try:
	cursor.execute(sql_insert)
	conn.commit()
except Exception as e:
	print(e)
	conn.rollback()



# print(conn)
# print(cursor)

cursor.close()
conn.close()
