// synchronous version
var fs = require('fs')

var readMe = fs.readFileSync('readMe.txt','utf8')
console.log(readMe)

//--------------------------------

fs.writeFileSync('writeMe.txt', readMe)

// ashycronous version
//------------------------------------

var readMe = fs.readFile('readMe.txt','utf8', function(err,data){
    console.log(data)
})

console.log('test') 