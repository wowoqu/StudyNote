var http = require('http');

http.createServer(function(req,res){
	throw new Error('Error!');
	res.writeHead(200,{'Content-Type':'text/plain'});
	res.write('hello world');
	res.end();
}).listen(8888);

process.on('uncaughtException',function(err){
	console.error(err);
	process.exit();
})
