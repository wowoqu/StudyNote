import sqlite3

conn = sqlite3.connect('testsqlite3.db')

cursor = conn.cursor()

# sql_creat = 'create table testtable\
# 			(id int primary key not null,\
# 			name text not null);'

sql_insert = "insert into testtable(\
				title,author)\
				values\
				('ABC','DEF')"

cursor.execute(sql_insert)
conn.commit()



sql_select = 'select * from testtable;'

cursor.execute(sql_select)

fin = cursor.fetchall()

for x in fin:
	print('id=%d,title=%s,author=%s'%x)




cursor.close()
conn.close()
