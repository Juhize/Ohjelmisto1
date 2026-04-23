'use strict'
//Valitaan html documentista ensimmäinen button
const nappi = document.querySelector('button');
//Luodaan nappiin eventlistener, mikä aktivoituu klikkauksesta
nappi.addEventListener('click', function(evt){
//Luodaan tapahtuma, mikä tapahtuu klikkauksesta
alert('The button has been clicked!');
});