'use strict'

const nimi = prompt('Tell me your name: ');
const hat = document.createElement('p');
document.body.appendChild(hat);

const num = Math.floor(Math.random()*3);
let team;

if (num === 0){
    team = "dirbydoub";
}
else if (num === 1){
    team = "durbledääm";
}
else{
    team = "batmään";
}

const result = `You are a ${team}`;
hat.innerHTML = result