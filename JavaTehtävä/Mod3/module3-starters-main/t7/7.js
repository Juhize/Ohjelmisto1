'use strict';

const targetElem = document.querySelector('#target');
const targetTxt = document.querySelector('#trigger');

targetTxt.addEventListener('mouseover', function(over){
targetElem.src = "img/picB.jpg";
targetTxt.removeEventListener('mouseover');
});
targetTxt.addEventListener('mouseleave', function(off){
targetElem.src = "img/picA.jpg";
});