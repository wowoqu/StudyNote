var net = require('net');

var count = 0;
var users = {};

var server = net.createServer(function(conn) {
    // console.log('new connection');
    conn.setEncoding('utf8');
    var nickname;
    conn.write('Welcome to ' + count + ' other peopel are connected at this time.\r\nplease write your name and press enter:');
    count++;

    var buf = '';

    conn.on('data', function(data) {
        // console.log(data.toString());
        // conn.write(':');
        if (data == '\r\n') {
            // data = data.replace('\r\n', '');
            console.log(buf);
            if (!nickname) {
                // console.log(users[data]);
                if (users[data]) {
                    conn.write('nickname aleady in use. try again:');
                    return;
                } else {
                    nickname = buf;
                    users[nickname] = conn;

                    for (var i in users) {
                        users[i].write(nickname + 'joined the room\r\n');
                    }
                    // users[nickname].write(nickname + ' : ');
                }
            } else {
                // conn.write(':')
                for (var i in users) {
                    if (i != nickname) {
                        users[i].write(nickname + ':' + buf + '\r\n');
                    }
                }
                // users[nickname].write(nickname + ' : ');
            }
            buf = '';
        } else {
            buf += data;
        }
    });

    conn.on('close', function() {
        count--;
        delete users[nickname];

        for (var i in users) {
            if (i != nickname) {
                users[i].write(nickname + ' left \r\n');
            }
        }
    });

});
server.listen(8000, function() {
    console.log('server listening on : 8000');
});

// var client = net.connect(8000,'localhost');
// client.on('connect',function(){

// });



function broadcast(msg, exceptMyself) {
    for (var i in users) {
        if (!exceptMyself || i != nickname) {
            users[i].write(msg);
        }
    }
}
