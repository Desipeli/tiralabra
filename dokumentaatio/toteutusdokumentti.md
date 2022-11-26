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

## Suorituskyky
[Suorituskykytestien](https://github.com/Desipeli/tiralabra/blob/main/dokumentaatio/testausdokumentti.md#Suorituskyky) perusteella asteen kasvaessa myös tallennukseen kuluva aika kasvaa lineaarisesti

