var net = require('net');

var client = net.connect(8000,'127.0.0.1');
client.on('connect',function(){
	console.log('connect is link');
});
