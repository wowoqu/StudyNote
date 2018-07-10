#创建库
var Base = {                     //创建一个对象
    getId : function(id){
        return document.getElementById(id):  //创建库并添加获取元素方法。
    }
}
##连缀方法
function Base(){
    this.elements = \[\];   //创建一个类；
    this.getId = function(id){
        this.elements.push(document.getElementById(id));
        return this;      //连缀用
    };
    this.getName = function(name){
        var names = document.getElementsByName(name);
        for(var i = 0; i < names.length; i++){
            this.element.push(names\[i\]);
        }
        return this;
    }
    this.getTagName = function(tag){
        var tags = document.getElementsByTagName(tag);
        for(var i = 0; i < tags.length; i++){
            this.elements.push(tags);
        }
        return this;
    }
}
###添加原型函数
Base.prototype.click = function(fn){
    for(var i = 0; i < this.elements.length; i++){
        this.elements\[i\].onclick = fn;
    }
};
Base.prototpye.css = function(attr,value){
    if(arguments.length == 2){
        for(var i = 0; i < this.elements.length; i++){
            this.elements\[i\].style\[attr\] = value;
        }
        return this;
    } else{
        return this.elements\[i\].style\[attr\];
    }
}
Base.prototype.html = function(str){
    if(arguments.length != 0){
        this.elements.innerHTML = str;
    } else{
        return this.elements.innerHTML;
    }
}

####逻辑：遍历，判断是否与正则 (前面为空或没有后面为空或没有 )匹配。
####如果为false 则添加class
Base.prototype.addClass = function(className){
    for(var i = 0; i < this.elements.length; i++){
        if(!this.elements\[i\].className.match('\\s|^' + className + '\\s|$')){
            this.elements\[i\].className += '' + className;
        }
    }
    return this;
}
####逻辑：遍历，判断是否 与正则匹配，替换为'' 即可。
Base.prototype.removeClass = function(className){
    for(var i = 0; i < this.elements.length; i++){
        if(this.elements\[i\].className.match('\\s|^' + className + '\\s|$')){
            this.elements\[i\].className = this.elements\[i\].className.
            replace('\\s|^' + className + '\\s|$','');
        }
    }
    return this;
}
Base.prototype.hide = function(){
    this.elements\[i\].style.display = 'none';
    return this;
}
Base.prototype.show = function(){
    this.elements\[i\].style.display = 'block';
    return this;
}
##鼠标移入移出
Base.prototype.hover = function (over, out) {
    for (var i = 0; i < this.elements.length; i ++) {
        this.elements[i].onmouseover = over;
        this.elements[i].onmouseout= out;
    }
    return this;
}
###居中效果 
###逻辑：获取当前页面可视区宽高减去本身宽高  得出结果在除以2 即使当前可视区的中心的 左上角。而本身则在最中心位置。 
Base.prototype.center = function (width, height) {
    var top = (document.documentElement.clientHeight - width) / 2;
    var left = (document.documentElement.clientWidth - height) / 2;
    for (var i = 0; i < this.elements.length; i ++) {
        this.elements[i].style.top = top + 'px';
        this.elements[i].style.left = left + 'px';
    }
    return this;
}
###锁屏 逻辑：获取视口的宽高并设置锁屏 ，显示
在html中创建一个空div并调用方法。
Base.prototype.lock = function(){
    this.elements.style.width = window.innerWidth + 'px'
    this.elements.style.height = widow.innerHeight + 'px'
    this.elements.styel.display = 'block';
}
###解锁 
Base.prototype.unlock=function(){
    for(vari = 0; i < this.elements.length; i++){
        this.elements[i].style.display='none';
    }
}
###拖拽
####逻辑：当鼠标按下时获取当前 位置到可视区左上角的宽 (e.clientX)和高
####并获取自己本身的左上角到可视区左上角 的宽 (this.offsetLeft)和高
####获取当前位置到自己本身左上角的 宽(第一个减第二个或者是 e.offsetX | Firefox的为e.layerX)和高
####当鼠标移动时，让本身左上角 (this.left)减去点击位置到自己本身左上角的差即可 。
####当鼠标移出时，将鼠标按下和鼠标移动设为null  。
####设置不能移出浏览器边缘，判断left (本身左上角位置) 是否小于0 (left<0证明left在屏幕左边缘再往左) 
####移动最小即为左上角left = 0；top = 0；移动最大即为右下角 left = window.innerWidth(浏览器可视区域宽度) - this.offsetWidth(自己本身宽度) 以这两个条件判断即可 。
####指定哪种标签可以拖拽 ：判断e.target.targetName == tagName;然后执行主程序即可。
Base.prototype.drag = function () {
    for (var i = 0; i < this.elements.length; i ++) {
        this.elements[i].onmousedown = function (e) {
            var e = window.event;
            var _this = this;
            var diffX = e.clientX - _this.offsetLeft;
            var diffY = e.clientY - _this.offsetTop;
            
            document.onmousemove = function (e) {
                var e = getEvent(e);
                _this.style.left = e.clientX - diffX + 'px';
                _this.style.top = e.clientY - diffY + 'px';
            } 
            document.onmouseup = function () {
                this.onmousemove = null;
                this.onmouseup = null;
            }
        };
    }
    return this;
}


###W3C现在绑定(addEventListener)实现的功能
+ 支持同一元素的同一事件句柄可以绑定多个监听函数(click,fn1),(click,fn2),执行时顺序执行。
+ 如果在同一元素的同一事件句柄上多次注册同一个函数，则只执行一次(click,fn1),(click,fn1)(这个不执行)  
+ 函数体内的this指向的是当前正在处理事件的节点


###为避免前台new一个对象，在库中封装一个变量
var $ = function(_this){
    this.elements = \[\]; \\存贮当前环境上下文this
    if(_this != undefined){
        this.elements\[0\] = _this;
    }
    return new Base();
}
###插件 : 创建方法，设置一个可传函数的参数 ，原型链方法指向这个函数。
Base.prototype.extend = function(name,fn){
    Base.prototype\[name\] = fn
}
###调用 ：创建一个js文件 
$().extend('drag',function(tag){...})
###DOM加载顺序
+ HTML解析完毕
+ 外部脚本和样式加载完毕
+ 脚本在文档内解析并执行
+ HTML DOM完全构造起来
+ 图片和外部内容加载；
+ 网页加载完成

###传统加载方法
+ window.onload  这种方法是在图片加载完成之后在执行的
+ 另一种方法
+  if(document.addEventListener){
    addEventListener(document,'DOMContentLoaded',function(){})  
}    这种方法是在DOM结构加载完成时执行的。   
###JS的宽和高总结
+ 只有在Event对象里才会出现X和Y
+ clientX，clientY 以浏览器左上角为原点，从原点到鼠标点击位置的距离
+ screenX, screenY 以屏幕左上角为原点，从原点到鼠标点击位置的距离。
+ offsetX, offsetY 以自身左上角为原点，从原点到鼠标点击位置的距离。
+ pageX，pageY 以页面左上角为原点(当页面滚动时，与clientX不同，没有滚动条时相同)，从原点到鼠标点击位置的距离。

+ Width和Height一般指的都是长度和宽度，left与top一般指的是与
+ 
