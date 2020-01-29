var http = require('http')
var fs = require('fs')

var myReadStream = fs.createReadStream(__dirname + '/stream.txt','utf8')//this funtion inherite from eventEmitter so we can use the methods
var myWriteStream = fs.createWriteStream(__dirname + '/writeMee.txt')

myReadStream.on('data', function(chunk){
    console.log('new chunk received :')

    myWriteStream.write(chunk)
    console.log('new chunk writen')
 //   console.log(chunk) 
})



  // new method PIPE qui fait la meme chose que readstream et write stream
// pipe remplace tout de la ligne 7 a 13

myReadStream.pipe(myWriteStream) 