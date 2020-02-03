var http = require('http')
var fs = require('fs')

var myReadStream = fs.createReadStream(__dirname + '/stream.txt','utf8')//this funtion inherite from eventEmitter so we can use the methods


var server = http.createServer(function(req,res){
    console.log('request was made:'+req.url)
    res.writeHead(200,{'Content-Type':'application/json'}) // change plain/text to html to the browser know what to do bc of the css etc....

    var myObj = {
        name: 'ryu',
        job: 'ninja',
        age: 29
    }
   res.end(JSON.stringify(myObj)) // bc we cant send response in form of an object we need to make it json

})

server.listen(3000, '127.0.0.1')
console.log('Listening to port 3000')