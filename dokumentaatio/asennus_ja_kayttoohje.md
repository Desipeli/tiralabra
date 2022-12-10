# Vaatimukset

- python 3.8 tai uudempi
- poetry 1.2.2 tai uudempi. Huom ei toimi versiolla 1.1!

# Asennus

Kloonaa repositorio omalle koneelle, ja suorita komento `poetry install` hakemistossa `lausegeneraattori`

## Käynnistys Linuxilla

Suorita komento `poetry run invoke start` hakemistossa `lausegeneraattori`

## Käyttö Windowsilla

Suorita komento `poetry run python src\index.py` hakemistossa `lausegeneraattori`

## GUI

Käyttöliittymä koostuu vasemmalla olevasta toimintopalkista, sekä suurimman osan ikkunaa kattavasta tekstilaatikosta.
- Toiminnot:
  - `Lataa tiedostoja`: Voit valita kerralla useita .txt päätteisiä tiedostoja, joiden sisältö tallennetaan trieen.
  - `Vaihda aste`: Aste voi olla mikä tahansa positiivinen kokonaisluku tai nolla (ei tuota mitään järkevää). Mitä suurempi aste sitä pidemmät latausajat. Toimii parhaimmillaan välillä 2-4, suuremmilla asteilla muodostetut lauseet alkavat olla deterministisiä. ``Asteen vaihtaminen tyhentää muistin``
  - `Muodosta lause`: Muodostaa lauseen jos ohjelmaan on ladattu dataa. Tekstilaatikkoon voi kirjoittaa valmiiksi sanoja, jolloin ohjelma pyrkii jatkamaan lausetta niiden perusteella. Jos tekstilaatikko on tyhjä, arpoo ohjelma jonkin isolla kirjaimella alkavan sanan.
  - `Muodosta tarina`: voidaan muodostaa tekstiä, jonka minimipituus (välimerkit lasketaan tässä sanoiksi) on alapuolella olevan kentän arvo.
  - `Kopioi`: Kopioi tekstin leikepöydälle
  - `Tyhjennä`: Tyhjentää tekstilaatikon
  - `Tyhjennä muisti`: Tyhjentää trien.
  

## Tekstikäyttöliittymä

En suosittele, graafinen on helpompi käyttää. Voidaan käynnistää Linuxilla `poetry run python3 src/index.py teksti`, ja Windowsilla `poetry run python src\index.py teksti` hakemistossa `lausegeneraattori`

- Päävalikossa syötetään komentoa vastaava numero/kirjain ja painetaan `enter`
  - 1: Voidaan vaihtaa Markovin ketjun astetta. Jos ohjelmaan on jo ladattu tiedostoja, niiden tiedot katoavat tämän komennon jälkeen. Asteen on oltava 0 tai suurempi kokonaisluku
  - 2: Ohjelma pyytää tiedoston nimeä. Syötä `lausegeneraattori/data` hakemistossa olevan tekstitiedoston nimi. Muista tiedostopääte! Esimerkiksi `tiedosto.txt`. Vaihtoehtoisesti voit kirjoittaa isolla `KAIKKI`, jolloin ohjelmaan ladataan kaikki data-kansiossa olevat tiedostot
  - 3: Ohjelma pyytää alkusanoja. Voit jättää kentän tyhjäksi, jolloin kaikki sanat arvotaan. Jos kirjoitat tähän yhden tai useamman sanan, pyrkii ohjelma jatkamaan kirjoittamaasi tekstiä.
  - 4: Sama kuin kohta 3, mutta ensin kysytään teksitin minimipituutta, vastaus kokonaislukuna.
  - t: Tulostaa Trien solmujen lukumäärän
  - q: Sulkee ohjelman
  - h: Tulostaa päävalikon vaihtoehdot
  
## Testaus

- Suorita komento `poetry run invoke testcov` hakemistossa `lausegeneraattori`
- Testikattavuusraportti tallentuu kohteeseen `lausegeneraattori/htmlcov/index.py`

## Lint

- Suorita komento `poetry run invoke lint` hakemistossa `lausegeneraattori`
