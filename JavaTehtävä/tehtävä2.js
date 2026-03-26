'use strict'
const nimi = prompt('Type your name.');
const greeting = `Hello ${nimi}`;
const teksti = document.createElement('p');
teksti.innerHTML = greeting;
document.body.appendChild(teksti);

