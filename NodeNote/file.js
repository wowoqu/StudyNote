// var fs = require('fs');

// fs.readFile('./index.txt',function(err,data){
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('异步读取： ' + data.toString());

// });

// var data = fs.readFileSync('index.txt');
// console.log('同步读取： ' + data.toString());

// var fs = require('fs');

// console.log('准备打开文件！');

// fs.stat('index.txt', function(err, stats) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log(stats);
//     console.log('读取文件信息成功！');
//     console.log("是否为文件(isFile) ? " + stats.isFile());
//     console.log("是否为目录(isDirectory) ? " + stats.isDirectory());
// })

// var fs = require('fs');   //获取fs对象

// console.log('It is ready to write');

// fs.writeFile('input.txt','I am a file for write',function(err){
// 	if (err) {                    //调用writeFile方法 ，err为传的第一个对象
// 		return console.error(err);
// 	}
// 	console.log('write is over');
// 	console.log('----------');
// 	console.log('It is time to read');
// 	fs.readFile('input.txt',function(err,data){   //如果不报错，读取文件
// 		if (err) {
// 			return console.error(err);
// 		}
// 		console.log('It is Sync to read file data: ' + data.toString());

// 	});
// });

// var fs = require('fs');

// var buf = new Buffer(1024);

// console.log('ready for alreay file');

// fs.open('input.txt','r+',function(err,fd){
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('file is open');
// 	console.log('It is time to reay file');
	
// 	var data = fs.ftruncate(fd,2,function(err,data){
// 			if (err) {
// 				console.log(err);
// 			}
// 		});
// 	console.log(data);

// 	fs.read(fd,buf,0,buf.length,0,function(err,bytes,buffer){
// 		if (err) {
// 			return console.error(err);
// 		}
// 		console.log(bytes + 'bytes has been read');

// 		if (bytes > 0) {
// 			console.log(buf.slice(0,bytes).toString());
// 			console.log(buffer.slice(0,bytes).toString());
// 		}

// 	})
// 	fs.close(fd,function(){
// 		console.log('read is close');
// 	})

// })

var fs = require('fs');

fs.readdir('./',function(err,files){
	if (err) {
		console.error(err);
	}

	files.forEach(function(items,index){
		console.log(index + ' : ' + items);
	});

});

