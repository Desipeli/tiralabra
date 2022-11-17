# Vaatimukset

- python 3.8 tai uudempi
- poetry 1.2.2 tai uudempi

# Asennus

Kloonaa repositorio omalle koneelle, ja suorita komento `poetry install` hakemistossa `lausegeneraattori`

# Käyttö (Linux)

Suorita komento `poetry run invoke start` hakemistossa `lausegeneraattori`

Ohjelmassa on tällä hetkellä vain tekstikäyttöliittymä, joka toimii seuraavanlaisesti:
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