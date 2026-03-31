// Write a program that prompts the user for five numbers and prints them in the reverse
//  order they were entered (not reverse sorted). Print the result to the console.(2p)

//     Save the numbers to an array, then use for-loop to iterate in reverse order.
//     Do not use array.reverse() function.

'use strict'

let num;
let dice = 5;
const numbers = [];

while (dice != 0){
    num = prompt(`Give a ${dice}. number: `);
    numbers.push(num);
    dice -= 1
}

for (let i = 4; i >= 0; i--) {
        console.log(`Number: ${numbers[i]}`);
}
