#一些最重要的SQL命令
+ SELECT - 从数据库中提取数据
+ UPDATE - 更新数据库中的数据
+ DELETE - 从数据库中删除数据
+ INSERT INTO - 向数据库中插入新数据
+ CREATE DATABASE - 创建新数据库
+ ALTER DATABASE - 修改数据库
+ CREATE TABLE - 创建新表
+ ALTER TABLE - 变更（改变）数据库表
+ DROP TABLE - 删除表
+ CREATE INDEX - 创建索引（搜索键）
+ DROP INDEX - 删除索引

##SQL SELECT 语法
> select column_name,column_name
> from table_name;

> select * from table_name

##SELECT DISTINCT 语句用于返回唯一不同的值。
>select distinct column_name,column_name
>from table_name;

##SQL WHERE 语句
###WHERE 子句用于提取那些满足指定标准的记录
>SELECT column_name,column_name
>FROM table_name
>WHERE column_name operator value;

##实例
>select * from websites where country = 'CN';

##WHERE 子句中的运算符
+ =
+ <>
+ \>
+ <
+ \>=
+ <=
+ between 在某个范围内
+ like 搜索某种模式
+ in 指定针对某个列的多个可能值。

>Select * from emp where sal in (5000,3000,1500);

>% 表示多个字值，_ 下划线表示一个字符；
>Select * from emp where ename like '_M%'; 表示前面有一个任意的字符第二个是M，然后后面有任意多个字符。

##SQL AND & OR 运算符
###AND & OR 运算符用于基于一个以上的条件对记录进行过滤。
###SQL AND & OR 运算符
>如果第一个条件和第二个条件都成立，则 AND 运算符显示一条记录。
>如果第一个条件和第二个条件中只要有一个成立，则 OR 运算符显示一条记录。

>SELECT column_name,column_name
>FROM table_name
>ORDER BY column_name,column_name ASC|DESC; 
>asc顺序，从小到大，desc逆序，从大到小

>select * from test order by title desc; 默认是从小到大；
>select * from test order by title,author desc;  可以按多列排序

##SQL INSERT 语法
###INSERT INTO 语句可以有两种编写形式。
###第一种形式无需指定要插入数据的列名，只需提供被插入的值即可：
>INSERT INTO table_name
>VALUES (value1,value2,value3,...);
###第二种形式需要指定列名及被插入的值：
>INSERT INTO table_name (column1,column2,column3,...)
>VALUES (value1,value2,value3,...);

###实例
    insert into test (title,author)
    values ('123','456');

    insert into test values (12,'abc','def'); # id , title ,author 必须把所有的数据写全。

##SQL UPDATE 语句
###UPDATE 语句用于更新表中已存在的记录。
###SQL UPDATE 语法
>UPDATE table_name
>SET column1=value1,column2=value2,...
>WHERE some_column=some_value;

###实例
>update test set title = 'update',author = 'abc' where title = '123'
>没有where时 必须要小心，是直接将一列的数据全部改写了。

##SQL DELETE 语句
###DELETE 语句用于删除表中的行。
###SQL DELETE 语法
>DELETE FROM table_name
>WHERE some_column=some_value;

##实例
>delete from test where title = '123'

##SQL关于删除的三个语句，DROP;TRUNCATE;DELETE的区别。
##DROP:
>DROP test;

删除表test，并释放空间，将test删除的一干二净。
##TRUNCATE:
>TRUNCATE test;

删除表test里的内容，并释放空间，但不删除表的定义，表的结构还在。

##DELETE:
###1、删除指定数据
删除表test中年龄等于30的且国家为US的数据
>DELETE FROM test WHERE age=30 AND country='US';
###2、删除整个表
仅删除表test内的所有内容，保留表的定义，不释放空间。
>DELETE FROM test 或者 DELETE FROM test;
>DELETE * FROM test 或者 DELETE * FROM test;

>创建表时可以添加的选项 engine = innodb charset = utf8



#Sqlite3 Note
##以下是一些相关提示
+ sqlite3没有数据库的列表，必须cd进你创建的数据库所在的文件夹下，然后运行 ```sqlite3 数据库名 记得带上后缀 创建新数据库的命令与这个一样```   
+ 创建一个新的数据库 ```sqlite3 数据库名加.db后缀 该命令是有该数据库时进入，没有时直接创建。该命令是在命令行没有进入sqlite3时下敲的
+ .help 查看帮助信息
+ .tables 查看所有表信息
+ .databases 查看数据库信息，必须在当前目录下刚刚创建的才能看到。或者进入到数据库内运行.databases 看到数据库的文件位置。
##查询表结构 .schema 表名
###SQL中的为 desc 表名
