# ECMAScript6 Note

## let和const命令
### 1. let命令

ES6新增了`let`命令，用来声明变量。它的用法类似与`var`，但是所声明的变量，只在`let`命令所在的代码块内有效。

    {
        let a = 10;
        var b = 1;
    }

    a  //ReferenceError : a is not defined.在括号包围的代码块中有效，代码块以外不可调用
    b //1

`for`循环的计数器，就很适合`let`命令

    var a = [];
    for(var i = 0; i < 10; i++){
        a[i] = function(){
            console.log(i);
        }
    }
    a[6]();  //10 闭包，

    var a = []
    for(let i = 0; i < 10; i++){
        a[i] = function(){
            console.log(i);
        }
    }
    a[6]();  //6 

上面代码中，变量`i`是`let`声明的，当前的`i`只在本次循环有效，所以每一次循环的`i`其实都是一个新的变量，所以最后输出的是`6`。你可能会问，如果每一轮循环的变量`i`都是重新声明的，那它怎么知道上一轮循环的值，从而计算出本轮循环的值？这是因为 `JavaScript` 引擎内部会记住上一轮循环的值，初始化本轮的变量i时，就在上一轮循环的基础上进行计算。

`var`命令会发生"变量提升"现象，即变量可以在声明之前使用，值为`undefined`。
`let`声明的变量一定要在声明语句后使用，否则报错。

    console.log(foo) //输出undefined
    var foo = 2;

    console.log(bar)  //报错ReferenceError
    let bar = 2;   

> 相关链接 [http://es6.ruanyifeng.com/#docs/let](link)

> 阮一峰React ：[http://www.ruanyifeng.com/blog/2016/09/react-technology-stack.html](link)  
