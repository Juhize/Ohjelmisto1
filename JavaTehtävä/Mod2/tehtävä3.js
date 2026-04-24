// Write a program that asks for the names of six dogs. 
// The program prints dog names to unordered list <ul> in reverse alphabetical order.
'use strict';
let numDogs = 6;
const dogs = [];
const listDogs = document.querySelector('ul');

while (numDogs > 0){
    let doggie = prompt(`Give a dog number ${numDogs}. name: `);
    dogs.push(doggie);
    numDogs -= 1;
}
dogs.sort().reverse();
dogs.forEach(function(item){
    const dog = document.createElement('li');
    dog.innerText = item;
    listDogs.appendChild(dog);
});