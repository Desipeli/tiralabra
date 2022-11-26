# Toteutusdokumentti

## Ohjelman rakenne

Luokat:
- Trie ja TrieSolmu: Nämä muodostavat yhdessä trie-tietorakenteen. Lisättävät sanat tallennetaan Trieen TrieSolmu-olioina.
- Arpa: Tarjoaa toiminnot satunnaisoperaatiota varten.
- Jasennin: Tekstin jäsentäminen oikeaan muotoon ja sen muuttaminen listaksi ennen Trieen tallentamista. Muuttaa myös Triestä saadun listan sanoja tekstiksi, samalla jäsentäen sen haluttuun muotoon.
- Ohjelma: Ohjaa päätoiminnallisuuksia, eli edellisten luokkien avulla tallentaa tekstin Trieen muistiin ja hakee sieltä sanoja lauseita muodostettaessa.
- TiedostonLukija: Tarjoaa toiminnot tiedostojen lukemiselle.
- GUI: Graafinen käyttöliittymä, jonka avulla ladataan tiedostoja ja käytetään ohjelmaa.

