var stuff = require('./stuff')

console.log(stuff.counter(['shaun','crystal','ryu']));

var events = require('events'); // core module in nodejs

var myEmitter = new events.EventEmitter()
myEmitter.on('someEvent', function(msg){
    console.log(msg);
});


myEmitter.emit('someEvent', 'the event was emited');


//----------------------------------------------------

var util = require('util') //inherite objects etc..

var Person = function(name){
    this.name = name;

}
util.inherits(Person, events.EventEmitter)


var james = new Person('james')
var mary = new Person('mary')
var kilua = new Person('kilua')

var people = [james,mary,kilua]

people.forEach(function(person){
    person.on('speak', function(msg){
        console.log(`${person.name} said : ${msg}`)
    })
})

james.emit('speak','yeahhhhhh !')