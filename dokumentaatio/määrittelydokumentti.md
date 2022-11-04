# Määrittelydokumentti

Dokumentaation kieli: suomi
Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti
Projekti toteutetaan pythonilla
Vertaisarvioitavat projektit mielellään pythonilla toteutettuja

## Aihe

Tarkoituksena on luoda Markovin ketjujun avulla toimiva koneoppimisalgoritmi, joka muodostaa uusia lauseita syötetyn tekstin perusteella. Ohjelmalle syötetty teksti tallennetaan sanoina itse totetutettuun trie-tietorakenteeseen. Markovin ketjun asteluku määritetään datan syötön yhteydessä.

Valitsin kyseisen aiheen, koska en ole toteuttanut mitään vastaavaa ja se vaikuttaa kiinnostavalta.

## Trie

Trie-tietorakenne on puu, jonka jokaisella solmulla voi olla mielivaltainen määrä lapsisolmuja. Solmuissa on linkki niiden lapsisolmuihin, sekä tieto siitä, kuinka monta kertaa kyseisen solmun avain on esiintynyt. Markovin ketjun aste määrää puun syvyyden: aste + 1. Esimerkki: toisen asteen ketjua varten on tallennettava kolmen sanan jonoja, sillä kolmas sana riippuu kahdesta edellisestä.

Tilavaativuus: O(n)
- Kaikki syötteen sanat tallennettaan Trieen pahimmillaan (aste + 1) * n 
    - Tässä siis aste voi olla myös nolla, jolloin sanat olisivat riippumattomia toisistaan

Aikavaativuudet:
- Lisäys: O(n), jossa n on lisättävien sanojen määrä
- Haku: O(n), jossa n on puun syvyys
- solmun poisto: O(n)

## Markovin ketju

Projektissani hyödyntämä Markovin ketju toimii siten, että lauseita muodostettaessa uusi lisättävä sana riippuu vain tietystä määrästä(aste) aikaisempia sanoja. Jos on useampia vaihtoehtoja valita seuraava sana, arvotaan se mahdollisista vaihtoehdoista perustuen esiintymistiheyteen.

## Ohjelman toimintaidea

Yksinkertainen esimerkki miten ohjelma toimisi 2.asteen ketjulla:
Ohjelmalle syötetty data (sanoja): A B B A B C A B C
- Valitaan arpomalla mikä tahansa sana: saadaan esimerkiksi B todennäköisyydellä 4/9.
- Valittu B. Nyt voidaan valita mikä tahansa sana, joka esiintyy syötteessä B:n jälkeen. Valitaan A todennäköisyydellä 1/3.
- Valittu B A. Nyt ainoa vaihtoehto on lisätä perään B, sillä syötteessä esiintyy B A vain yhdessä kohtaa.
- Valittu B A B. Nyt vaihtoehtoina on B tai C, sillä toisen asteen ketjussa tarkastellaan vain kahta edellistä, eli sanajonoa A B. Todennäköisyys että valitaan B on 1/3 ja todennäköisyys että valitaan C on 2/3.

## Lähteet

[https://en.wikipedia.org/wiki/Trie](https://en.wikipedia.org/wiki/Trie)
[https://en.wikipedia.org/wiki/Markov_chain](https://en.wikipedia.org/wiki/Markov_chain)
[https://www.youtube.com/watch?v=i3AkTO9HLXo&t=193s&ab_channel=NormalizedNerd](https://www.youtube.com/watch?v=i3AkTO9HLXo&t=193s&ab_channel=NormalizedNerd)
