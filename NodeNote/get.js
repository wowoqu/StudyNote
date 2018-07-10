var http = require('http');
var url = require('url');
var util = require('util');

http.createServer(function(request,response){
	response.writeHead(200,{'Content-Type':'text/html;charset=utf-8'});
	response.write(util.inspect(url.parse(request.url,true)));
	response.write('<br />' + url.parse(request.url).pathname);
	response.end();
}).listen(8888);
