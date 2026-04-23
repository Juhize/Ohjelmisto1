'use strict';

const nappi = document.querySelector('#start');
const operation = document.querySelector('#operation')
const result = document.querySelector('#result')
const num1 = document.querySelector('#num1')
const num2 = document.querySelector('#num2')
nappi.addEventListener('click', function(evt){
    if (operation.value == 'add')
    result.innerHTML = `${Number(num1.value) + Number(num2.value)}`
    else if (operation.value == 'sub')
    result.innerHTML = `${Number(num1.value) - Number(num2.value)}`
    else if (operation.value == 'multi')
    result.innerHTML = `${Number(num1.value) * Number(num2.value)}`
    else if (operation.value == 'div')
    result.innerHTML = `${Number(num1.value) / Number(num2.value)}`
});