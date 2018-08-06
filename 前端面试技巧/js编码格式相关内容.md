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

### JavaScript 类型数组
    JavaScript类型化数组是一种类似数组的对象，并提供了一种用于访问原始二进制数据的机制。 正如你可能已经知道，Array 存储的对象能动态增多和减少，并且可以存储任何JavaScript值。JavaScript引擎会做一些内部优化，以便对数组的操作可以很快。然而，随着Web应用程序变得越来越强大，尤其一些新增加的功能例如：音频视频编辑，访问WebSockets的原始数据等，很明显有些时候如果使用JavaScript代码可以快速方便地通过类型化数组来操作原始的二进制数据将会非常有帮助。

    但是，不要把类型化数组与正常数组混淆，因为在类型数组上调用  Array.isArray()  会返回false。此外，并不是所有可用于正常数组的方法都能被类型化数组所支持（如 push 和 pop）。

### 缓冲和视图
    为了达到最大的灵活性和效率，JavaScript 类型数组（Typed Arrays）将实现拆分为缓冲和视图两部分。一个缓冲（由 ArrayBuffer 对象实现）描述的是一个数据块。缓冲没有格式可言，并且不提供机制访问其内容(即ArrayBuffer不可修改)。为了访问在缓冲对象中包含的内存，你需要使用视图(Typed Array或者Date View)。视图提供了上下文 — 即数据类型、起始偏移量和元素数 — 将数据转换为实际有类型的数组。

### 类型数组视图(Typed Array View)
    类型化数组视图具有自描述性的名字和所有常用的数值类型像Int8，Uint32，Float64 等等。有一种特殊类型的数组Uint8ClampedArray。它仅操作0到255之间的数值。例如，这对于Canvas数据处理非常有用

- Int8Array -128 to 127 1   8-bit two's complement signed integer   byte    int8_t
- Uint8Array  0 to 255    1   8-bit unsigned integer  octet   uint8_t
- Uint8ClampedArray   0 to 255    1   8-bit unsigned integer (clamped)    octet   uint8_t
- Int16Array  -32768 to 32767 2   16-bit two's complement signed integer  short   int16_t
- Uint16Array 0 to 65535  2   16-bit unsigned integer unsigned short  uint16_t
- Int32Array  -2147483648 to 2147483647   4   32-bit two's complement signed integer  long    int32_t
- Uint32Array 0 to 4294967295 4   32-bit unsigned integer unsigned long   uint32_t
- Float32Array    1.2x10-38 to 3.4x1038   4   32-bit IEEE floating point number ( 7 significant digits e.g. 1.1234567)    unrestricted float  float
- Float64Array    5.0x10-324 to 1.8x10308 8   64-bit IEEE floating point number (16 significant digits e.g. 1.123...15)   unrestricted double double

#### 示例
    使用试图和缓冲
首先，我们创建一个16字节固定长度的缓冲。

    var buffer = new ArrayBuffer(16);    
现在我们有了一段初始化为0的内存，目前还做不了什么太多操作。让我们确认一下数据的字节长度：
    
        if (buffer.byteLength === 16) {
          console.log("Yes, it's 16 bytes.");
        } else {
          console.log("Oh no, it's the wrong size!");
        }
在实际开始操作这个缓冲之前，需要创建一个视图。我们将创建一个视图，此视图将把缓冲内的数据格式化为一个32位的有符号整数数组：

    var int32View = new Int32Array(buffer);
现在我们可以像普通数组一样访问该数组中的元素：

    for (var i = 0; i < int32View.length; i++) {
      int32View[i] = i * 2;
    }
该代码会将数组以0, 2, 4和6填充 （一共4个4字节元素，所以总长度为16字节）。

### 同一数据的多个视图
你可以在同一数据上创建多个视图，但每种不同的视图只能创建一个，第二个将获取不到值。例如：基于上文的代码，我们可以添加如下代码处理：

    var int16View = new Int16Array(buffer);
    
    for (var i = 0; i < int16View.length; i++) {
      console.log("Entry " + i + ": " + int16View[i]);
    }
这里我们创建了一个2字节整数视图，该视图共享上文的4字节整数视图的缓冲，然后以2字节整数打印出缓冲里的数据，这次我们会得到0, 0, 2, 0, 4, 0, 6, 0这样的输出。

### 将视图转化为普通数组
    var int8View = new Uint8Array(buffer)
    var s = Array.from(int16View);

### 将普通数组转化为视图
    var s = [1,2,3,4]
    var int8View = new Uint8Array(s);

### ArrayBuffer 实例常用方法和属性

#### 属性
ArrayBuffer实例都会从ArrayBuffer.prototype继承属性和方法。

    ArrayBuffer.prototype.byteLength 只读
数组的字节大小。在数组创建时确定，并且不可变更。
#### 方法
    ArrayBuffer.prototype.slice()
返回一个新的 ArrayBuffer ，它的内容是这个 ArrayBuffer 的字节副本，从begin（包括），到end（不包括）。如果begin或end是负数，则指的是从数组末尾开始的索引，而不是从头开始。

### [TypedArray](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)



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

### [相关链接](https://developer.mozilla.org/zh-CN/docs/Web/API/FileReader)

### 笔记
#### 文件流
    当你想读取本地文件，或者是通过表单上传文件时，如果是上传文件则需要设置ajax传输文件内容(直接用jqueryajax库即可)。如果是读取本地文件则需要创建一个FileReader对象。
    FileReader对象获取表单或者其他地方的File对象，并创建FileReader对象，通过FileReader对象的readAsArrayBuffer方法将文件流转换为ArrayBuffer流。
#### ArrayBuffer流
    ArrayBuffer流可通过new ArrayBuffer(length)创建，也可通过FileReader的
    readAsArrayBuffer获取，获取到的ArrayBuffer不可操作，但可以转换为视图操作。
#### TypedArray流
    TypedArray与DataView()都是可以操作原始ArrayBuffer流，常用的typedArray有Uint8Array,Uint16Array,Uint32Array,FloatArray64,分别是一个字节两个字节三个字节四个字节。
    一个ArrayBuffer可以创建多个不同类型的视图，多个视图之间可以相互转化。
#### TypedArray流之间的相互转化
初始化一个8个字节的ArrayBuffer流

    var buffer = new ArrayBuffer(8)
创建多个不同类型的typedbuffer流

    var u8 = new Uint8Array(buffer);
    var u16 = new Uint16Array(buffer);
    var u32 = new Uint32Array(buffer);
    var f64 = new Float64Array(buffer);
这几个类型的数据之间可以互相转化。

    u8[0] = 12  // [12,0,0,0,0,0,0,0]
    u16 : [12,0,0,0]
    u32 : [12,0]
    f64 : [6e-323] // 可能采用不同的计数方法 或者是科学记数法等。 科学记数法和数字之间的转换下次再考虑。

    u8为一个字节最大存贮为255 当存贮超过255时将自动减去256
例如：

    u8[0] = 255  // [255,0,0,0,0,0,0,0]
    u8[0] = 256  // [0,0,0,0,0,0,0,0]
    u8[0] = 257  // [1,0,0,0,0,0,0,0]
    如果有u16则u16自动转化为响应的数字，上面的示例为255，0，1
当超过一个字节存贮量时，转用两个字节存贮，则u8与u16都将自动转换
例如：

    u16[0] = 256  // [256,0,0,0] 
    u8[0]// [0,1,0,0,0,0,0,0]  // 自动转换，第二位为1时，代表一个256，两个的话代表两个256
    位数说明： 第一个0是2的0次方个256乘以0，第二个0为2的1次方个256乘以1，以此类推。
u8，u16，u32大小说明
    
    u8 2**8 = 256
    u16 2**16 = 65536
    u32 2**32 = 4294967296

#### 常用的字符转换思路
    思路一： base64
    js需要传输的字符串中如果有中文，一般需要用encodeURIcomponent将中文转换为字符串，(因为字符串转化为base64不允许有中文，转化会报错)之后使用btoa(str)进行base64的转化。
    之后在通过str.charCodeAt(index)转换为ascii编码。
    知识点： 因为英文或者一般的符号只占用一个字节，但是中文或者个别特殊符号占用的字节比较多，这时就需要考虑用什么格式转化为ArrayBuffer流，如果转化的字符串中有中文的话，则不能用ASCII，只能用UTF-8或者Unicode编码方式，而解码字节流的时候也需要相同的编码方式去解码。
    base64编码的特点是，将字符串中的所有中文或者特殊符号encodeURIcomponent处理后再btoa之后就只有英文字母或者一般的符号，即所有的字符都可用ascii表示，都可以通过以一个字节存贮。 


    思路二 ： utf-8
    将需要发送的字符串转化为UTF-8格式的字节流。上传到服务器，然后服务器将获取的字节流通过decode解码成utf-8格式的字符串。这里通过str.charCodeAt(index)进行处理的长度可能超过256所以不为Ascii编码，再从服务器获取到数据时需要将字节流转换为string类型的数据则需要String.fromCharCode()进行处理。
#### 常用的字节流切分
    (从浏览器获取数据)可以创建一个原生字节流ArrayBuffer对象接收原始数据，然后创建一个Uint8Array的视图，通过切分自己创建的Uint8Array对数据进行切分。
    如果是拼接数据的话则可以采用视图下标进行处理。

#### 浏览器对字节流进行处理
    如果是从本地上服务器上传文件或者上传json字符串，浏览器会将数据转化为字节流上传到服务器，如果是中文字符一般是添加encodeURIcomponent进行处理然后上传到服务器，编码格式默认是UTF-8，服务器获取到的数据需要进行decode处理。


    如果是服务器向浏览器发送数据，则会自动进行decode处理，并通过utf-8编码方式进行转化，浏览器一般获取不到服务器发过来的buffer流，一般接收的都是已经处理好的字符串，这里要说明一点，如果服务器进行过base64加密，通过浏览器会自动进行解密的。
    如果浏览器需要获取原始的buffer流的话，则需要资金进行转换，将字符串转化为buffer字节流。
