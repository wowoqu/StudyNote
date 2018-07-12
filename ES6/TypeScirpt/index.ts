let isDone: boolean = true;
let decLiteral: number = 0xf00d;
let names: string = 'Gene';
let s1: string = "i'm " + names;
let s2: string = `i'm ${names}`
console.log(s1 + ' ' + s2);
console.log(isDone + ' ' + decLiteral);

let blist: string[] = ['1','2','3'];
let blists: Array<string> = ['1','2','3'];

let x: [string, number] = ['wowoqu',2];
x[2] = '23'
console.log(x.length);
for(let j in x){
    console.log(typeof(x[j]));
}
//枚举
enum Color {red,green,blue}
let c: Color = Color.blue;
let bc: string = Color[1]

console.log(bc);

console.log(`c: ${c}`);

let list: any[] = [1,true,'123'];

function warnUser(): void {
    alert('123');
}
warnUser();

let typelist: any = '321';

let s3: number = (<number>typelist);
alert(s3);
let a;
function foo(){
    let a;
    return a;
}

console.log(foo());
function thecity(){
    let getCity;

    if(true){
        let city = 'sdf';
        getCity = function(){
            return city;
        }
    }
    return getCity();
}
var getPrice = function(){
    return 4.55;
}
var bgetprice = () => 4.55;

let arr = ['1','2','3'];

let breakfast = arr.map(fruit => {
    return fruit + 's';
});
console.log(breakfast);

function kbs(...args: any[]){
    console.log(args)
}
kbs(1,2,3,4,5);

function getCar(make: any, model: any, value: any){
    return {
        make,
        model,
        value,

        ['make' + make]: true,

        depreciate(){
            this.value -= 2500;
        }
    };
}

let car = getCar('ba', 'le', 40000);

var meMao = new DOMStringMap()