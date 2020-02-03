
//  WE WANT TO RENDER THE VIEWS AND NOT SEND RESPONSE FILE like in app.js file

var express = require('express')
var bodyParser = require('body-parser')
var app = express() // to acess methods and make everything easyer 

var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.set('view engine', 'ejs') // let know express that we use ejs pakage
app.use('/assets', express.static('assets')) // GOOD EXPLANATION  : the first argument passed in the use function is basically
                                             // saying that anyone who tries to access files inside /assets should be served with the files inside the "stuff" dir,
                                             // which is the second parameter of the use function.




// HTTP Methode : GET,POST,DELETE,PUT
app.get('/',function(req,res){
    res.render('index')
})

//to render we use render method N.B : EJS know automatically to see in views FILE to search for ejs views so we render the name of the file !! magic! 
app.get('/home',function(req,res){
    res.render('index')
})

app.get('/contact',function(req,res){
    res.render('contact',{qs: req.query})
})

app.post('/contact', urlencodedParser, function(req,res){   //urlencoderParser give us acces to body proprety and body is the informations the users submited
    console.log(req.body)
    res.render('contact-success', {data:req.body})
})


app.get('/profile/:name', function(req,res){
    var data = {age: 29, job: 'ninja',hobbies:['eating','fighting','fishing']}
    res.render('profile', {person: req.params.name, data:data}) 
})

app.get('/*',function(req,res){    // handle routing errors (the '*' mean everything else )
    res.render('404')
})



app.listen(3000)