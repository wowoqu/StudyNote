#PythonNote

##匿名函数

> lambda 参数：式子
> lambda x,y:x+y
> 变量 = lambda x,y:x+y
> func = lambda x,y:x+y
> 调用匿名函数：func(1,2)
> 不需要return，默认有返回值。

###案例一

```
stus = [{'name':'zhangsan','age':18},
        {'name':'lisi','age':19},
        {'name':'wangwu','age':20},
    ]
```

###按name排序：

```
 stus.sort(key = lambda x:x['name'])
```

###按age排序：
```
stus.sort(key = lambda x:x['age'])
```

###案例二

    def test(a,b,func):
        result = func(a,b)
        print(result)

    test(11,22,lambda x,y:x+y) 定义一个可以自由变换的函数

###案例二改

    func_new = input('请输入一个匿名函数：')
    func_new = eval(func_new)
    test(11,22,func_new)

##使用Python DB API访问数据库流程

+ 开始
+ 创建connection
+ 获取cursor
    - 执行查询
    - 执行命令
    - 获取数据
    - 处理数据
+ 关闭cursor
+ 关闭connection
+ 结束

##DB API -数据链接对象connection
+ host
+ port
+ user
+ passwd
+ db
+ charset

##connection方法
+ cursor
+ commit
+ rollback
+ close

##DB 示例

    import MySQLdb

    conn = MySQLdb.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'test',
        charset = 'utf8'    
        )

    cursor = conn.cursor()

    print(conn)

    cursor.close()
    conn.close()

##cursor对象方法
+ execute(op[,args])        执行一个数据查询和命令
+ fetchone()                获取结果集的下一行
+ fetchmany(size)           获取结果集的下几行
+ fetchall()                获取结果集中剩下的所有行
+ rowcount                  最近一次execute返回数据的行数或影响的行数
+ close()                   关闭游标对象

##示例
    import MySQLdb

    conn = MySQLdb.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'test',
        charset = 'utf8'    
        )
    #简便写法
    conn = MySQLdb.Connect('localhost','root','123456','testpython')

    cursor = conn.cursor()

    sql = 'select * from user'
    cursor.execute(sql)

    rs = cursor.fetchall()
    for row in rs:
        print('userid=%s,username=%s'%row)

    print(conn)

    cursor.close()
    conn.close()

#示例try形式
    try:
        cursor.execute(insert)
        cursor.execute(update)
        cursor.execute(delete)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()
