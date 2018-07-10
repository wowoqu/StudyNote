#SHELL NOTE
###注释：
###\#!/bin/bash \#!跟shell命令的完全路径。作用：显示后期命令以哪种shell来执行这些命令。如果不指明shell，以当前shell作为执行的shell
    [root@abc]#ll /bin/sh
    lrwxrwxrwx.1 root root 4 Dec 18 2017 /bin/sh -> bash

###\#This is to show what a example looks like. shell中以#开头表示，整个行被当作注释
###shell程序一般以.sh结尾

###创建shell程序的步骤：
+ 第一步：创建一个包含命令和控制结构的shell文件
+ 第二步：修改这个文件的权限使它可以执行 ```chmod u+x```
+ 第三步：执行
    * 方法1：./example
    * 方法2：使用绝对路径 [root@abc]\# /root/test/example01.sh
    * 方法3：[root@abc]\# bash example01.sh

##shell 变量
###变量是shell传递数据的一种方法，变量是用来代表每个值的符号名。
###shell有两类变量：临时便量和永久变量。

####临时变量：是shell程序内部定义的，其使用范围仅限于定义它的程序，对其它程序不可见
####永久变量：是环境变量，其值不随shell脚本的执行结束而消失。 ```echo $PATH```
####使用变量值时，要在变量名前加上前缀"$"
####变量赋值：赋值号"="两边应没有空格

