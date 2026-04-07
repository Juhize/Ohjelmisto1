'use strict';

const targetElem = document.querySelector('#target');
const targetTxt = document.querySelector('#trigger');

function vaihto(){
    targetElem.src = "img/picB.jpg";
}
targetTxt.addEventListener('mouseover', vaihto);