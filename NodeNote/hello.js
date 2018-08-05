'use strict';

let s = 'Hello';

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
// 	greet,
// 	hi,
// 	goodbye
// }
