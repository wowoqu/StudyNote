# js 编码格式相关内容

## 了解编码格式

### 字节
    一个字节相当于8个bit 即8个 0000 0000 二进制表示

### ASCII
    ASCII编码为一个字节编码8个bit位，一般最高位为0，不为0的一般不是ASCII，只适用英文字母及一些符号

### Unicode
    Unicode编码一般为两个字节即16个bit位，偏僻的用4个字节，即使英文字母可以用一个字节代替还是用两个字节

### UTF-8
    UTF-8编码是把一个Unicode字符根据不同的大小编译成1-6个字节。小的字符如英文字母用一个字节代替，大的字母如汉字用多个字符代替。

### 使用
    在内存中 统一使用Unicode编码 如打开的记事本为Unicde编码
    在硬盘中的数据为UTF-8编码，如将文件保存到硬盘为UTF-8编码
    需要传输的时候也是用的UTF-8编码的

### FileReader对象
    允许Web应用程序异步读取存储在用户计算机上的文件（或原始数据缓冲区）的内容，使用File 或 Blob 对象指定要读取的文件或数据。

#### 构造函数
var file = new FileReader()
    
    返回一个新构造的FileReader。

#### 事件处理

FileReader.onload

    处理load事件。该事件在读取操作完成时触发

#### 方法
FileReader.abort()

    中止读取操作。在返回时，readyState属性为DONE。
FileReader.readAsArrayBuffer()

    开始读取指定的 Blob中的内容, 一旦完成, result 属性中保存的将是被读取文件的 ArrayBuffer 数据对象.
FileReader.readAsBinaryString() 

    开始读取指定的Blob中的内容。一旦完成，result属性中将包含所读取文件的原始二进制数据。
FileReader.readAsDataURL()

    开始读取指定的Blob中的内容。一旦完成，result属性中将包含一个data: URL格式的字符串以表示所读取文件的内容。
FileReader.readAsText()

    开始读取指定的Blob中的内容。一旦完成，result属性中将包含一个字符串以表示所读取的文件内容。

### ArrayBuffer
    用来表示通用的、固定长度的原始二进制数据缓冲区。ArrayBuffer 不能直接操作，而是要通过类型数组对象或 DataView 对象来操作，它们会将缓冲区中的数据表示为特定的格式，并通过这些格式来读写缓冲区的内容

### Blob
    表示一个不可变、原始数据的类文件对象。Blob 表示的不一定是JavaScript原生格式的数据。File 接口基于Blob，继承了 blob 的功能并将其扩展使其支持用户系统上的文件

### String.fromCharCode()
    静态 String.fromCharCode()方法返回使用指定的Unicode值序列创建的字符串。
#### 示例
    String.fromCharCode(65,66,67) // 返回字符串ABC

### str.charCodeAt(index)
    返回值是一表示给定索引处（String中index索引处）字符的 UTF-16 代码单元值的数字；如果索引超出范围，则返回 NaN

#### 用法
    "ABC".charCodeAt(0) // returns 65:"A"

### Uint8Array
    Uint8Array 数组类型表示一个8位无符号整型数组，创建时内容被初始化为0。创建完后，可以以对象的方式或使用数组下标索引的方式引用数组中的元素。

#### 语法格式
    Uint8Array(length);//创建初始化为0的，包含length个元素的无符号整型数组
    Uint8Array(typedArray);
    Uint8Array(object);
    Uint8Array(buffer [, byteOffset [, length]]);

### btoa
    WindowOrWorkerGlobalScope.btoa()  从 String 对象中创建一个 base-64 编码的 ASCII 字符串，其中字符串中的每个字符都被视为一个二进制数据字节。

#### 实例
    let encodedData = window.btoa("Hello, world"); // base64 编码
    let decodedData = window.atob(encodedData); // 解码 成 ASCII

#### Unicode字符串

在各浏览器中,使用 window.btoa 对Unicode字符串进行编码都会触发一个字符越界的异常.
先把Unicode字符串转换为UTF-8编码,可以解决这个问题。
    
    function utf8_to_b64( str ) {
    return window.btoa(unescape(encodeURIComponent( str )));
    }
    function b64_to_utf8( str ) {
        return decodeURIComponent(escape(window.atob( str )));
    }
    // Usage:
    utf8_to_b64('? à la mode'); // "4pyTIMOgIGxhIG1vZGU="
    b64_to_utf8('4pyTIMOgIGxhIG1vZGU='); // "? à la mode"
    //译者注:在js引擎内部,encodeURIComponent(str)相当于escape(unicodeToUTF8(str))
    //所以可以推导出unicodeToUTF8(str)等同于unescape(encodeURIComponent(str))    

### atob()
    WindowOrWorkerGlobalScope.atob() 对用base-64编码过的字符串进行解码 。你可以使用 window.btoa() 方法来编码一个可能在传输过程中出现问题的数据，并且在接受数据之后，使用 atob() 方法再将数据解码。例如：你可以编码、传输和解码操作各种字符，比如0-31的ASCII码值。
    
    关于针对Unicode或者UTF-8的应用方面，请查看 this note at Base64 encoding and decoding  和 this note at window.btoa()。

相关链接： [https://developer.mozilla.org/zh-CN/docs/Web/API/FileReader](link)
