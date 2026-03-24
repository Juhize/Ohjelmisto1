'use strict'
const otsikko = document.querySelector('#otsikko')
otsikko.innerHTML = "Esimerkki";
const nimi = prompt('Type your name.');
const greeting = `Hello ${nimi}`;
const teksti = document.createElement('p');
const uusi = document.createElement('p2');
teksti.innerHTML = greeting;
document.body.appendChild(teksti);
document.body.appendChild(uusi);
const luku = 1+2+3;
const lasku = `1+2+3=${luku}`;
uusi.innerHTML = lasku;
console.log("I'm printing to console!");