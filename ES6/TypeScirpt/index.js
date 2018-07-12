"use strict";
var isDone = true;
var decLiteral = 0xf00d;
var names = 'Gene';
var s1 = "i'm " + names;
var s2 = "i'm " + names;
console.log(s1 + ' ' + s2);
console.log(isDone + ' ' + decLiteral);
var blist = ['1', '2', '3'];
var blists = ['1', '2', '3'];
var x = ['wowoqu', 2];
x[2] = '23';
console.log(x.length);
for (var j in x) {
    console.log(typeof (x[j]));
}
//枚举
var Color;
(function (Color) {
    Color[Color["red"] = 0] = "red";
    Color[Color["green"] = 1] = "green";
    Color[Color["blue"] = 2] = "blue";
})(Color || (Color = {}));
var c = Color.blue;
var bc = Color[1];
console.log(bc);
console.log("c: " + c);
var list = [1, true, '123'];
function warnUser() {
    alert('123');
}
warnUser();
var typelist = '321';
var s3 = typelist;
alert(s3);
var a;
function foo() {
    var a;
    return a;
}
console.log(foo());
function thecity() {
    var getCity;
    if (true) {
        var city_1 = 'sdf';
        getCity = function () {
            return city_1;
        };
    }
    return getCity();
}
var getPrice = function () {
    return 4.55;
};
var bgetprice = function () { return 4.55; };
var arr = ['1', '2', '3'];
var breakfast = arr.map(function (fruit) {
    return fruit + 's';
});
console.log(breakfast);
function kbs() {
    var args = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        args[_i] = arguments[_i];
    }
    console.log(args);
}
kbs(1, 2, 3, 4, 5);
function getCar(make, model, value) {
    var _a;
    return _a = {
            make: make,
            model: model,
            value: value
        },
        _a['make' + make] = true,
        _a.depreciate = function () {
            this.value -= 2500;
        },
        _a;
}
var car = getCar('ba', 'le', 40000);
var meMao = new DOMStringMap();
