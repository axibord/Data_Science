var http = require('http')
var fs = require('fs')

var myReadStream = fs.createReadStream(__dirname + '/stream.txt','utf8')//this funtion inherite from eventEmitter so we can use the methods

myReadStream.on('data', function(chunk){
    console.log('new chunk received :')
    console.log(chunk)
})

  