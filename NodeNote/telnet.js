var http = require('http');
http.createServer(function(req,res){
	res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'});
	res.write('<h1>Hello world</h1>');
	console.log('is run')
	res.end();
}).listen(8000);
