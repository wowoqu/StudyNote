process.on('exit',function(code){
	setTimeout(function(){
		console.log('该代码不会执行');
	},1000);

	console.log('退出代码为：',code);
	console.log(process.versions);
	console.log(process.pid);
	console.log(process.title);
});
console.log('程序执行结束');
