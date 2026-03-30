// Write a program that rolls user defined number of dice and displays the sum of the results of the dice rolls.

//     First, program asks the user for the number of dice rolls.
//     Then the program throws a die as many times as the user defined.
//     Print the sum of the results in the console or in the HTML document.

'use strict'

const hat = document.createElement('p');
document.body.appendChild(hat);

let num;
let result = 0;
let dice = Number(prompt('Number of dice: '));
const numbers = [];
let i;

while (dice != 0){
    num = Math.floor(Math.random()*6)+1;
    numbers.push(num);
    dice -= 1
}
for (i of numbers){
    result += Number(i)
}

hat.innerHTML = `You threw number <strong>${numbers.join(", ")}</strong><br>The sum of <strong>${numbers.length} dice is <strong style ="color: red; font-size: x-large">${result}</strong>`;