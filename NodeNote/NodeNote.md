# 创建Node.js应用
## CommonJS规范
### 加载模块
    var http = require('http');
### 导出模板
    function greet(){...}
    module.exports = greet;
### exports VS module.exports
    exports与module.exports一样，但是exports只能赋值导出一个对象，不可以导出数组
    module.exports则可以导出为数组或者对象。

#### 示例
    function greet(name) {
        console.log(s + ',' + name + '!');
    }
    function hi(name) {
        console.log('Hi, ' + name + '!');
    }
    function goodbye(name) {
        console.log('GoodBye, ' + name + '!');
    }
    exports.greet = greet;
    exports.hi = hi;
    exports.goodbye = goodbye;
    // module.exports = {
    //  greet,
    //  hi,
    //  goodbye
    // }
    // 虽然两种方法导出不一样不过在导入接收时是一样的
虽然两种方法都可用，但一般用的最多的是module.exports这种方法。

#### 调用
    // 代码可以通用两种方式的导入
    'use strict';
    const hello = require('./hello');
    let s = 'Michael';
    hello.greet(s);
    hello.goodbye(s);

## 基本模块
### global
    在js中有且仅有一个全局对象window，而在node.js中也有唯一的全局对象global，这个全局对象可同过cmd交互环境中输入 global.console 获得

### process
    process也是Node.js提供的一个对象，它代表当前Node.js进程。通过process对象可以拿到许多有用信息：
#### process.cwd() // 返回当前工作目录
    JavaScript程序是由事件驱动执行的单线程模型，Node.js也不例外。Node.js不断执行响应事件的JavaScript函数，直到没有任何响应事件的函数可以执行时，Node.js就退出了。

    如果我们想要在下一次事件响应中执行代码，可以调用process.nextTick()：











### 创建服务器
    var http = require('http');
    
    http.createServer(function(request,response){
        response.writeHead(200,{'Content-Type':'text/plain'});
        response.write('hello world')
        response.end();   //必须写end否则页面一直加载。
                        //如果end内写着东西，则会相应两个请求一个是/favicon.ico
        }).listen(8888);  //监听8888端口

## Node.js事件循环
Node.js 是单进程单线程应用程序，但是通过事件和回调支持并发，所以性能非常高。
Node.js 的每一个 API 都是异步的，并作为一个独立线程运行，使用异步函数调用，并处理并发。
Node.js 基本上所有的事件机制都是用设计模式中观察者模式实现。
Node.js 单线程类似进入一个while(true)的事件循环，直到没有事件观察者退出，每个异步事件都生成一个事件观察者，如果有事件发生就调用该回调函数.
## 事件驱动程序
Node.js 使用事件驱动模型，当web server接收到请求，就把它关闭然后进行处理，然后去服务下一个web请求。
当这个请求完成，它被放回处理队列，当到达队列开头，这个结果被返回给用户。
这个模型非常高效可扩展性非常强，因为webserver一直接受请求而不等待任何读写操作。（这也被称之为非阻塞式IO或者事件驱动IO）
在事件驱动模型中，会生成一个主循环来监听事件，当检测到事件时触发回调函数。

+ 引入events模块
    * var events = require('events');
+ 创建eventEmitter对象
    * var eventEmitter = new events.EventEmitter();
+ 绑定事件处理程序
    * eventEmitter.on('eventName',eventHandler);
+ 程序触发事件
    * eventEmitter.emit('eventName');

### 实例
    // 引入 events 模块
    var events = require('events');
    // 创建 eventEmitter 对象
    var eventEmitter = new events.EventEmitter();

    // 创建事件处理程序
    var connectHandler = function connected() {
       console.log('连接成功。');
      
       // 触发 data_received 事件 
       eventEmitter.emit('data_received');
    }

    // 绑定 connection 事件处理程序
    eventEmitter.on('connection', connectHandler);
     
    // 使用匿名函数绑定 data_received 事件
    eventEmitter.on('data_received', function(){
       console.log('数据接收成功。');
    });

    // 触发 connection 事件 
    eventEmitter.emit('connection');

    console.log("程序执行完毕。");
    
    改程序先触发connection事件 然后调用connectHandler方法，从该方法中在继续调用data_received事件。
