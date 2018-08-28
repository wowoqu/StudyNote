# WebPack Note
## npm package.json
package.json 文件至少要有两部分内容：

- “name” 
    + 全部小写，没有空格，可以使用下划线或者横线
- “version” 
    + x.x.x 的格式
    + 符合“语义化版本规则”

非必要字段：

- description：描述信息，有助于搜索
- main: 入口文件，一般都是 index.js
- scripts：支持的脚本，默认是一个空的 test
- keywords：关键字，有助于在人们使用 npm search 搜索时发现你的项目
- author：作者信息
- license：默认是 MIT
- bugs：当前项目的一些错误信息，如果有的话

### 指定依赖包
当我们创建一个package包时，我们需要在package.json中指定项目需要的依赖，当项目部署时可通过`npm install`将项目所需的依赖包下载下来。
包有两种依赖方式：

- `dependencies`：在生产环境中需要用到的依赖
- `devDependencies`：在开发、测试环境中用到的依赖

在命令行中可设置依赖包是开发用的还是在生产时需要用的

    npm install webpack --save-dev  // --save-dev声明要安装的包是开发时用的
    npm install express --save  // --save声明要安装的包是生产时需要依赖的，当项目部署时会安装express依赖包
上面两个在package.json中的效果是：

    "description": {
        "express": "^2.13.0"
    },
    "devDependencies": {
        "webpack": "^4.17.1",
        "webpack-cli": "^3.1.0"
      }

### 语义化规范
如果只打算接受补丁版本的更新（也就是最后一位的改变），就可以这么写： 

- 1.0
- 1.0.x
- ~1.0.4

如果接受小版本的更新（第二位的改变），就可以这么写： 

- 1
- 1.x
- ^1.0.4

如果可以接受大版本的更新（自然接受小版本和补丁版本的改变），就可以这么写： 

- *
- x

### script字段用来声明脚本
    {
      "name": "demo",
      "scripts": {
        "lint": "jshint **.js",
        "test": "mocha test/"
      }
    }

调用的时候

    npm run lint
    npm run test

> npm run 是 npm run-script 的缩写。

<br/>
> npm run 会创建一个Shell，执行指定的命令，并临时将node_modules/.bin加入PATH 变量，这意味着本地模块可以直接运行。

[原文链接](https://blog.csdn.net/u011240877/article/details/76582670/)

## 开始使用webpack
### 安装
- 创建package包
    + npm init -y
- 安装相关依赖包
    + npm install --save-dev webpack
    + npm install webpack-cli --save-dev(webpack4以上需要安装)
- 创建webpack.config.js文件(不创建也可以使用，不过创建更容易使用)
    + 新建文件webpack.config.js
    + 设置webpack.config.js中相应的字段
- 创建开发项目app文件夹(待打包的项目)
- 创建发布(部署)项目public文件夹(打包到本文件夹下)

#### webpack.config.js
    const path = require('path');
    module.exports = {
        entry: __dirname + '/app/index.js',  //入口文件,从这个文件开始打包
        output: {                           // 出口文件，所有的项目打包到这个目录下
            filename: 'bundle.js',
            path: path.resolve(__dirname, 'public/js')
        },
        module: {
            rules: [                        // 相关规则设置
                {
                    test: /\.css$/,         // 设置css
                    use: [
                        'style-loader',
                        'css-loader'
                    ]
                },
                {
                    test: /\.(png|svg|jpg|gif|jpeg)$/,
                    use: [                  // 设置图片
                        'file-loader'
                    ]
                }
            ]
        }
    };
#### package.json
    {
      "name": "SegmentWP",
      "version": "1.0.0",
      "description": "",
      "private": true,
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "build": "webpack"
      },
      "keywords": [],
      "author": "",
      "license": "ISC",
      "devDependencies": {
        "css-loader": "^1.0.0",
        "file-loader": "^2.0.0",
        "style-loader": "^0.23.0",
        "webpack": "^4.17.1",
        "webpack-cli": "^3.1.0"
      }
    }
#### 项目目录
- node_modules
- app
    + hello.js
    + index.js
- public
    + js
        * bundle.js
    + index.html
- package.json
- webpack.config.js

#### 启动
    npm run build

### 生成Source Maps(便于调试)
开发总是离不开调试，方便的调试能极大的提高开发效率，不过有时候通过打包后的文件，你是不容易找到出错了的地方，对应的你写的代码的位置的，`Source Maps`就是来帮我们解决这个问题的。

通过简单的配置，webpack就可以在打包时为我们生成的`source maps`，这为我们提供了一种对应编译文件和源文件的方法，使得编译后的代码可读性更高，也更容易调试。
- source-map
- cheap-module-source-map
- eval-source-map
- cheap-module-eval-source-map

在webpack的配置文件中配置`source maps`，需要配置`devtool`。

中小型的开发环境一般采用`eval-source-map`。
#### webpack.config.js设置
    module.exports = {
      devtool: 'eval-source-map',
      entry:  __dirname + "/app/main.js",
      output: {
        path: __dirname + "/public",
        filename: "bundle.js"
      }
    }

### 使用webpack搭建本地服务器
想不想让你的浏览器监听你的代码的修改，并自动刷新显示修改后的结果，其实Webpack提供一个可选的本地开发服务器，这个本地服务器基于node.js构建，可以实现你想要的这些功能，不过它是一个单独的组件，在webpack中进行配置之前需要单独安装它作为项目依赖

    npm install --save-dev webpack-dev-server
#### devserver配置
- contentBase 
    + 默认webpack-dev-server会为根文件夹提供本地服务器，如果想为另外一个目录下的文件提供本地服务器，应该在这里设置其所在目录（本例设置到“public"目录）
- port    
    + 设置默认监听端口，如果省略，默认为”8080“
- inline  
    + 设置为true，当源文件改变时会自动刷新页面
- historyApiFallback  
    + 在开发单页应用时非常有用，它依赖于HTML5 history API，如果设置为true，所有的跳转将指向index.html

#### webpack.config.js
    module.exports = {
      devtool: 'eval-source-map',
      entry:  __dirname + "/app/main.js",
      output: {
        path: __dirname + "/public",
        filename: "bundle.js"
      },
      devServer: {
        contentBase: "./public",//本地服务器所加载的页面所在的目录
        historyApiFallback: true,//不跳转
        inline: true//实时刷新
      } 
    }

#### package.json 添加命令用于开启服务器
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "webpack",
        "server": "webpack-dev-server --open"
      },
[相关链接](https://segmentfault.com/a/1190000006178770)