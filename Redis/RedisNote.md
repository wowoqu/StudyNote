#Redis Note
##Window 安装
> 下载地址：https://github.com/MSOpenTech/redis/releases

解压并将文件夹重命名为redis，将路径配置到环境变量中。

>C:\redis>redis-server.exe redis.windows.conf

重新打开一个cmd窗口，进入目录
>C:\redis>redis-cli.exe -h 127.0.0.1 -p 6379
>127.0.0.1:6379> set myKey abc
>OK
>127.0.0.1:6379> get myKey
>"abc"
##Redis配置
[http://www.runoob.com/redis/redis-conf.html](link)

##Redis 数据类型
Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

###String(字符串)
string是redis最基本的类型，你可以理解成与Memcached一模一样的类型，一个key对应一个value。

string类型是二进制安全的。意思是redis的string可以包含任何数据。比如jpg图片或者序列化的对象 。

string类型是Redis最基本的数据类型，一个键最大能存储512MB。

###实例
    redis 127.0.0.1:6379> set name "runoob"
    OK
    redis 127.0.0.1:6379> get name
    "runoob"

##Hash（哈希）
Redis hash 是一个键值(key=>value)对集合。

Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。

###实例
    redis> hmset myhash field1 "Hello" field2 "World"
    "OK"
    redis> hget myhash field1
    "Hello"
    redis> hget myhash field2
    "World"
以上实例中 hash 数据类型存储了包含用户脚本信息的用户对象。 实例中我们使用了 Redis HMSET, HGETALL 命令，user:1 为键值。

每个 hash 可以存储 232 -1 键值对（40多亿）。

##List（列表）
Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。

###实例
    redis 127.0.0.1:6379> lpush runoob redis  //lpush从栈尾入栈
    (integer) 1                                 //rpus从栈首入栈
    redis 127.0.0.1:6379> lpush runoob mongodb  //lpop 栈尾出栈
    (integer) 2                                 //rpop 栈首出栈
    redis 127.0.0.1:6379> lpush runoob rabitmq
    (integer) 3
    redis 127.0.0.1:6379> lrange runoob 0 10
    1) "rabitmq"
    2) "mongodb"
    3) "redis"
    redis 127.0.0.1:6379>
列表最多可存储 232 - 1 元素 (4294967295, 每个列表可存储40多亿)。

##Set（集合）
Redis的Set是string类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。

###sadd 命令
添加一个string元素到,key对应的set集合中，成功返回1,如果元素已经在集合中返回0,key对应的set不存在返回错误。

>sadd key member

###实例
    redis 127.0.0.1:6379> sadd runoob redis
    (integer) 1
    redis 127.0.0.1:6379> sadd runoob mongodb
    (integer) 1
    redis 127.0.0.1:6379> sadd runoob rabitmq
    (integer) 1
    redis 127.0.0.1:6379> sadd runoob rabitmq
    (integer) 0
    redis 127.0.0.1:6379> smembers runoob
    
    1) "rabitmq"
    2) "mongodb"
    3) "redis"

注意：以上实例中 rabitmq 添加了两次，但根据集合内元素的唯一性，第二次插入的元素将被忽略。

集合中最大的成员数为 232 - 1(4294967295, 每个集合可存储40多亿个成员)。

##zset(sorted set：有序集合)
Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。
不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。

###zadd 命令
添加元素到集合，元素在集合中存在则更新对应score

>zadd key score member

###实例
    redis 127.0.0.1:6379> zadd runoob 0 redis
    (integer) 1
    redis 127.0.0.1:6379> zadd runoob 0 mongodb
    (integer) 1
    redis 127.0.0.1:6379> zadd runoob 0 rabitmq
    (integer) 1
    redis 127.0.0.1:6379> zadd runoob 0 rabitmq
    (integer) 0
    redis 127.0.0.1:6379> > ZRANGEBYSCORE runoob 0 1000
    1) "mongodb"
    2) "rabitmq"
    3) "redis"
