'use strict'

const answer = confirm('Should I calculate the square root?');
const hat = document.createElement('p');
document.body.appendChild(hat);

let num;
let calc;
let result;

if (answer == true){
    num = prompt('Number: ');
    if (num < 0)
        result = `Cannot define a square root of ${num}`;
    else{
        calc = Math.sqrt(num);
        result = `The square root of ${num} is ${calc}`;
    }
}

else{
    result = "The square root is not calculated.";
}

hat.innerHTML = result;