# StringBuilder
## javascript中的字符串链接问题。
创建两个字符串

    var str1 = 'hello';
    var str1 = 'world!';
    var allstr = str1 + str2;

### 代码执行过程
    先分配第一个字符串'hello'的内存
    在分配第二个字符串'world！'的内存
    开辟allstr的内存
    将str1的字符串复制到新内存，将str2复制到新内存
    把allstr指向新内存。
当有很多字符串连接时，就会出现效率问题。

### StringBuilder实现原理
    用Array对象存贮字符串，然后采用join方法连接字符串。
### 代码实现
    var array = new Array();
    array[0] = 'hello';
    array[1] = 'world!';
    var allstr = array.join('');
### 代码实现过程
    开辟存贮字符串的内存
    将每个字符串复制到新的内存
    allstr指向它。
### 网上现成的实现例子
[链接](https://www.cnblogs.com/loogn/archive/2011/06/22/2087442.html)
