'use strict'

const tvForm = document.querySelector('#tv');
tvForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const haku = document.querySelector('input[name=q]'.value);
  const kysely = `https://api.tvmaze.com/search/shows?q=${haku}`
  try{
    const raaka = await fetch(kysely);
    const jsonData = await raaka.json();
    console.log(jsonData);
  }catch(error){
    console.log(error.message);
  }
}
);