# Viikko 1

käytetty tuntimäärä n. 11

### Mitä olen tehnyt tällä viikolla?

- Triessä ohjelman kannalta oleellisimmat toiminnallisuudet, eli lisäys ja haku
  - Testaus ja docstring
  - mahdollisuus tulostaa syvyyshaku testausta varten
- Pääohjelma siirretty omaan luokkaan
  - Suurin osa riippuvuuksista injektoidaan, jotta testaaminen tulevaisuudessa helpompaa
- Jäsennin omassa luokassa ja testit olemassa
- tiedostonlukija omassa luokassa
- Luotu luokka "konsoli" syötteiden lukemista ja tulostamista varten
- Luotu luokka "apra" satunnisten kokonaislukujen generoimista varten
- Kaikki tarpeellinen kommentoitu docstringillä
- Testikattavuus saadan selville coveragen avulla
- taskit otettu käyttöön
  - käynnistys: invoke start
  - testikattavuus: invoke testcov
  - linttaus: invoke lint

### Miten ohjelma on edistynyt?

Triessä on ohjelman kannalta tärkeimmät ominaisuudet ja ohjelman rakennetta on paranneltu. Tiedoston lukemisen yhteydessä trieen tallennetaan asteen mukaan valitut sanajonot. Testikattavuus on tällä hetkellä vain 47%, sillä pääohjelmaa ei vielä testata.

### Mitä opin tällä viikolla?

Alkion hakeminen triestä, riippuvuuden injektoinnin hyöty ohjelman testaamisessa.

### Mikä jäi epäselväksi?

Tällä hetkellä kaikki selvää

### Mitä teen seuraavaksi?

- Aloitan testausdokumentin kirjoittamisen
- Ainakin jonkinlainen toimiva versio lauseen muodostuksesta trien avulla
- Aloitan integraatiotestauksen
