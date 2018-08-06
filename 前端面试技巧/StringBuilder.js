function StringBuilder(args) {
    this._strings = [];
    this._isBuild = false; //是否创建
    this._string = ""; //创建后的字符串
    for (var i = 0; i < arguments.length; i++) {
        this._strings.push(arguments[0]);
    }
}

StringBuilder.prototype.append = function(str) {
    this._strings.push(str);
    this._isBuild = false;
    return this;
}
//这个实现不太好....
StringBuilder.prototype.appendFormat = function(template, args) {
    if (arguments.length == 2 && typeof(args) == "object") {
        template = template.format(args);
    } else {
        var params = "";
        for (var i = 1; i < arguments.length; i++) {
            params += '"' + arguments[i] + '"';
            if (i != arguments.length - 1) {
                params += ",";
            }
        }
        eval("template =template.format(" + params + ")");
    }
    this._strings.push(template);
    this._isBuild = false;
    return this;
}

StringBuilder.prototype.toString = function() {
    if (!this._isBuild) {
        this._string = this._strings.join("");
    }
    return this._string;
}

//返回长度
StringBuilder.prototype.length = function() {
    if (!this._isBuild) {
        this._string = this._strings.join("");
    }
    return this._string.length;
}

// 删除最后几个字符
StringBuilder.prototype.del = function(lastNum) {
    var len = this.length();
    var str = this.toString();
    this._string = str.slice(0, len - lastNum);
    this._strings = [];
    this._strings.push(this._string);
    this.isBuild = true;
    return this;
}
