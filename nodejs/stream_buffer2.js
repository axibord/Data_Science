var http = require('http')
var fs = require('fs')

var myReadStream = fs.createReadStream(__dirname + '/stream.txt','utf8')//this funtion inherite from eventEmitter so we can use the methods


var server = http.createServer(function(req,res){
    console.log('request was made:'+req.url)
    res.writeHead(200,{'Content-Type':'text/html'}) // change plain/text to html to the browser know what to do bc of the css etc....

    var myReadStream = fs.createReadStream(__dirname + '/index.html','utf8')
    myReadStream.pipe(res) 
    
  

})

server.listen(3000, '127.0.0.1')
console.log('Listening to port 3000')