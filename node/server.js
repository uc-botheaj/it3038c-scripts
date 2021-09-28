var fs = require("fs");
var http = require("http");
var ip = require('ip');
var os = require("os");

var server = http.createServer(function (req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function (err, body) {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(body);
        });
    }
    else if (req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html = `
        <!DOCTYPE html>
            <html>
            <head>
                <title>Node JS Response</title>
                </head>
                <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: </p>
                <p>Total Memory: </p>
                <p>Free Memory: </p>
                <p>Number of CPUs: </p>
                </body>
            </html>
        `
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, { "Content-Type": "text/html" });
        res.end(`404 file not found at ${req.url}`);
    }
}).listen(3000)

console.log("Server listening on port 3000");