// Based on https://github.com/molnarg/node-http2

const fs = require('fs');
const http2 = require('http2');

var options = {
  key: fs.readFileSync('example.key'),
  cert: fs.readFileSync('example.crt')
};

http2.createServer(options, function(request, response) {
    response.end('Hello, here\'s some lovely Http\/2!');
}).listen(8001);
