'use strict';
const candidates = [];
let candNum = 0;
let numCandidates = parseInt(prompt("Number of candidates: "));
let empty = 0;
while (numCandidates > 0){
    candNum ++;
    let candidate = prompt(`Tell candidate number ${candNum} name: `);
    candidates.push({
    name: candidate,
    votes: 0
    });
    numCandidates--;
};
let voters = parseInt(prompt("Number of voters:"));
for (let i = 1; i <= voters; i++){
    let voteName = prompt('Who do you vote: ')
    for (let c = 0; c < candidates.length; c++){
        if (candidates[c].name === voteName){
            candidates[c].votes ++;
            break;
        }
        if (c === candidates.length - 1){
            empty++;
        }
    }
}
candidates.sort((a, b) => {
    return b.votes - a.votes;
});
console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log('Results:')
for (let j = 0; j < candidates.length; j++){
console.log(`Name: ${candidates[j].name} Votes: ${candidates[j].votes}`)
}
console.log(`Empty votes: ${empty}`)