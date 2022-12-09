# Toteutusdokumentti

## Ohjelman rakenne

Luokat:
- ``Arpa``: Tarjoaa toiminnot satunnaisoperaatiota varten.
- ``Trie ja TrieSolmu``: Nämä muodostavat yhdessä trie-tietorakenteen. Lisättävät sanat tallennetaan Trieen TrieSolmu-olioina. Trielle injektoidaan Arpa-olio, jolloin sitä voidaan testata luotettavasti huolimatta siitä, että normaalisti toimiessaan se arpoo joissain tilanteissa palauttamiaan sanoja.
- ``Jasennin``: Tekstin jäsentäminen oikeaan muotoon ja sen muuttaminen listaksi ennen Trieen tallentamista. Muuttaa myös Triestä saadun listan sanoja tekstiksi, samalla jäsentäen sen haluttuun muotoon.
- ``Ohjelma``: Ohjaa päätoiminnallisuuksia, eli edellisten luokkien avulla tallentaa tekstin Trieen muistiin ja hakee sieltä sanoja lauseita muodostettaessa.
- ``TiedostonLukija``: Tarjoaa toiminnot tiedostojen lukemiselle.
- ``GUI``: Graafinen käyttöliittymä, jonka avulla ladataan tiedostoja ja käytetään ohjelmaa. GUI:lle injektoidaan TiedostonLukija- sekä Ohjelma-olio.

Toiminta on siis jaettu kolmeen kerrokseen: GUI (Käyttöliittymä) --> Ohjelma (sovelluslogiikka) --> Trie (muisti/tietokanta)

## Suorituskyky ja tilavaativuus
- [Suorituskykytestien](https://github.com/Desipeli/tiralabra/blob/main/dokumentaatio/testausdokumentti.md#Suorituskyky) perusteella asteen tai sanamäärän kasvaessa myös tallennukseen kuluva aika kasvaa lineaarisesti. Trien solmujen määrä kasvaa myös lineaarisesti asteen kasvaessa. 
- Lauseen muodostus on normaalikäytössä (asteen ollessa alle 10) niin nopeaa, että eroja ei juuri huomaa. Lauseen muodostukseen kuluva aika on keskiarvoltaan alle 0.005 s. Jos triestä halutaan lauseen ensimmäiseksi sanaksi isolla alkukirjaimella alkava sana, saattaa siihen kulua hieman (0.001 - 0.003 s) enemmän aikaa.

## Perusteluja

### Sanan haku

- Trien funktio `hae` saa parametrina listan sanoja, joiden perusteella noudetaan uusi sana. Sanalistan pituus määrittää, kuinka syvältä puusta sana haetaan (Markovin ketjun aste). Aloitetaan siis tarkastelemalla trien juuresta, löytyykö sen lapsisolmuista sanalistan ensimmäistä sanaa. Jos löytyy, siirrytään siihen solmuun ja katsotaan, löytyykö sen lapsisolmuista listan seuraava sana jne. Jos päästään listan viimeistä sanaa vastaavaan solmuun asti, arvotaan jokin sana sen lapsisolmuista painottamalla sanojen esiintymistiheyttä. Arvonta joutuu pahimmassa tapauksessa käymään kertaalleen läpi kaikki lapsisolmut. Aikavaativuudeksi saadaan siis O(nm), jossa n on sanalistan pituus ja m on viimeisen solmun lapsisolmujen määrä. Tähän mennessä suoritettujen testien perusteella haku toimii käytännössä vakioajassa, sillä n:n ja m:n arvot pysyvät hyvin pieninä.
- Ohjelman tasolla sama operaatio toistetaan pahimmillaan n kertaa, joka kerta aina yhden sanan lyhyemmällä listalla. Sillä jos sanaa ei löydetä esimerkiksi kolmen sanan listalla `A B C`, kokeillaan seuraavaksi hakea listalla `B C`. Jos sanaa ei löydetä yhdenkään aikaisemman sanan perusteella, arvotaan jokin sana juuren alta.
