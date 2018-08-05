# Node.js 文件系统
    Node.js提供一组类似UNIX(POSIX)标准的文件操作API
## fs模块
    Node.js内置的fs模块是文件系统模块，负责读写文件。
    fs模块提供了同步和异步加载的方法。

同步操作的好处是代码简单，缺点是程序将等待IO操作，在等待时间内，无法响应其它任何事件。而异步读取不用等待IO操作，但代码较麻烦。

### 异步读取文件

    'use strict';
    var fs = require('fs');
    fs.readFile('sample.txt', 'utf-8', function (err, data) {
        if (err) {
            console.log(err);
        } else {
            console.log(data);
        }
    });
