'use strict'
const haku = document.querySelector('#haku')
const results = document.querySelector('#results')
haku.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const code = document.querySelector('#query').value;

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);
        const data = await response.json();
        
        for (const tvShow of data) {
            const artikkeli = document.createElement('article');
            artikkeli.addEventListener('click', function(evt){
                window.open(tvShow.show.url, '_blank');
            });
            
            const nimi = document.createElement('h2');
            nimi.textContent = tvShow.show.name;
            // Liitin css:n vanhasta tehtävästä, mikä huusi linkin toteuttamista toisella tavalla.
            // const linkki = document.createElement('a');
            // linkki.href = tvShow.show.url;
            // linkki.target = "_blank";
            // linkki.textContent = "Details";
            
            const kuva = document.createElement('img');
            kuva.src = tvShow.show.image?.medium || 'https://via.placeholder.com/210x295?text=No+Image';
            kuva.alt = tvShow.show.name;
            
            const kuvaus = document.createElement('div');
            kuvaus.innerHTML = tvShow.show.summary;

            const arvostelu = document.createElement('p')
            if (tvShow.show.rating?.average != null){
            arvostelu.innerText = tvShow.show.rating?.average;
            arvostelu.style.fontWeight = 'bold';
            }
            artikkeli.appendChild(nimi);
            artikkeli.appendChild(kuva);
            // artikkeli.appendChild(linkki);
            artikkeli.appendChild(kuvaus);
            artikkeli.appendChild(arvostelu);
            
            results.appendChild(artikkeli);
        }
        
    } catch (error) {
        console.log(error.message);
    }
}); //saatan ottaa omaan käyttöön :)