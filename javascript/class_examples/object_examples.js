'use strict';

// function Animal(type, noise, fur) {
//     console.log(arguments);
//     this.type = type;
//     this.fur = fur;
//     this.speak = function () {
//         console.log(noise)
//     }
// }
//
// var cat = new Animal('Cat', 'Meow', true);
// var dog = new Animal('Dog', 'Bork', false);
//
// var animal = {
//     type: 'Dog',
//     fur: true,
//     speak: function (noise) {
//         return noise
//
//     }
// };


function BankAccount(balance, name){
    this.balance = balance;
    this.name = name;
    this.withdraw = function (amount) {
        if (this.balance - amount > 0) {
            this.balance -= amount;
            console.log('Thank you ' + this.name + '. Your balance is $' + this.balance + '.')
        } else {
            console.log('I\'m sorry ' + this.name + '. You do not have enough funds. Your balance is $' + this.balance + '.' )
        }
    };
    this.deposit = function (amount) {
        this.balance += amount;
        console.log('Thank you ' + this.name + '. Your balance is $' + this.balance + '.')
    }
}

var chris = new BankAccount(100, 'Chris');
var chelsea = new BankAccount(500, 'Chelsea');
