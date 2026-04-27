'use strict'
const haku = document.querySelector('#haku')
haku.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const code = document.querySelector('#query').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error.message);
    }
});