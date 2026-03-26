'use strict'
const num1 = prompt('1st Number: ');
const num2 = prompt('2st Number: ');
const num3 = prompt('3st Number: ');
const plus = document.createElement('p');
document.body.appendChild(plus);
const lasku = `${num1}+${num2}+${num3}=${parseFloat(num1) + parseFloat(num2) + parseFloat(num3)}`;
plus.innerHTML = lasku;