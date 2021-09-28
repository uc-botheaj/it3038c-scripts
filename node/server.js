var http = require("http");

var server = http.createServer(function(req, res){
    res.writeHead(200, {"Content-Type":"text/text"});
    res.end("Hello from Node!")
});

server.listen(3000) 

console.log("Server listening on port 3000");