var http = require('http')

var server = http.createServer(function(reqer,res){
    console.log('request was made:'+reqer.url)
    res.writeHead(200,{'Content-Type':'text/plain'})
    res.end('response head worked')

})

server.listen(3000, '127.0.0.1')
console.log('Listening to port 3000')
