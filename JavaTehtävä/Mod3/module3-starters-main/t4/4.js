'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const targetElem = document.querySelector('#target');

for (let nimi of students) {
    targetElem.innerHTML += `<option value="${nimi.id}">${nimi.id} ${nimi.name}</option>`;
}