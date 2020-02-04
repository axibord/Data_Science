var express = require('express')

var app = express() // to acess methods and make everything easyer 

app.set('view engine', 'ejs') // let know express that we use ejs pakage

// HTTP Methode : GET,POST,DELETE,PUT
app.get('/',function(req,res){
    res.send('this is the homepage')
})

//to send html page we use : SendFile() method of express
app.get('/htmlpage',function(req,res){
    res.sendFile('/Users/aghiles/Desktop/data_science_git/Data_Science/nodejs/index.html')
})

app.get('/contact',function(req,res){
    res.sendFile('/Users/aghiles/Desktop/data_science_git/Data_Science/nodejs/contact.html')
})

app.get('/profile/:name', function(req,res){
    var data = {age: 29, job: 'ninja',hobbies:['eating','fighting','fishing']}
    res.render('profile', {person: req.params.name, data:data}) // we give the name of the view, we are passing" person " to the view " profile"  
})




app.listen(3000)
