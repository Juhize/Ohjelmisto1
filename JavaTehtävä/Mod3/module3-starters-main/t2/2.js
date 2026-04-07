'use strict';

const targetElem = document.querySelector('#target');

const felem = document.createElement('li');
const selem = document.createElement('li');
const telem = document.createElement('li');
selem.classList.add('my-item');
felem.innerHTML = 'First item';
selem.innerHTML = 'Second item';
telem.innerHTML = 'Third item';

targetElem.appendChild(felem);
targetElem.appendChild(selem);
targetElem.appendChild(telem);