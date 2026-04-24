// Write a program that asks the user for the number of participants. After this, the program asks for the names of all participants. 
// Finally, the program prints the names of the participants on the web page in an ordered list (<ol>) in alphabetical order. (2p)
'use strict'
const userlist = document.querySelector('ol');
const participants = [];
let users = prompt("Give me a number of participants: ");

while (Number(users) > 0){
    let part = prompt(`Tell user number ${users} name: `);
    participants.push(part);
    users--;
}
participants.sort();
participants.forEach(function(item){
    const user = document.createElement('li');
    user.innerText = item;
    userlist.appendChild(user);
});