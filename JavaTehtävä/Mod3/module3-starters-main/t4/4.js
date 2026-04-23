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
// Valitaan kohde html sivulta
const targetElem = document.querySelector('#target');
// Käytetään forEach metodia funktiona, mikä käy jokaisen listan olion läpi
students.forEach(function(student) {
// Luodaan HTML elementti (tila) = uusi option select-valikkoon
  const tila = document.createElement('option');
// Lisätään olion tiedot juuri tehtyyn tila-elementtiin
  tila.value = student.id;
  tila.textContent = student.name;
// Lisätään nyt valmis option-tila osaksi html sivua
  targetElem.appendChild(tila);
});