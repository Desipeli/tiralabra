# Testausdokumentti

## Yksikkötestaus

Yksikkötestit on suoritettu [unittest](https://docs.python.org/3/library/unittest.html) kirjaston avulla, ja testikattavuus saadaan [coveragella](https://coverage.readthedocs.io/en/6.5.0/). Testit ovat sijoitettuna aina testattavan luokan hakemistossa oleviin tests-kansioihin.
Testattavia luokkia ovat Trie, TrieSolmu, Jasennin ja Ohjelma. Käyttöliittymää ja satunnaistoimintoihin tarkoitettua Arpa-luokkaa ei testata.

Linux-ympäristössä testit voidaan suorittaa asennuksen jälkeen komennolla `poetry run invoke testcov`, jonka jälkeen testikattavuusraportti tallentuu kohteeseen `lausegeneraattori/htmlcov/index.html`. 

Viikon 3 testikattavuus: ![kuva](https://raw.githubusercontent.com/Desipeli/tiralabra/main/dokumentaatio/coverage_report_viikko_3.PNG)

## Luokkakohtaiset tiedot

### TrieSolmu

TrieSolmu testaus tapahtuu Trien testauksen välityksellä.

### Trie

Trieä testataan syöttämällä sille erilaisia 0-3 sanan listoja, joista se muodostaa solmuja. Testeillä varmistetaan, että Trie osaa luoda tarvittaessa uuden solmun, mutta että uutta solmua ei luoda jos sille ei ole tarvetta. Oikeellisuus varmistetaan tarkasetelemalla Trieä mm. syvyyshaulla.

Myös sanan valitsemista Triestä testataan erilaisten tilanteiden varalta, kuten:
- Mitä saadaan jos haetaan sanaa tyhjästä Triestä
- Toimiiko haku eri syvyyksillä
- Mitä jos yritetään hakea Trien syvyyttä syvemmältä
- Toimiiko isolla kirjaimella alkavan sanan hakeminen oikein

Koska sanan haku perustuu joissain tilanteissa satunnaisuuteen, on testejä varten luotu luokat `StubArpa1` ja `StubArpa`, jotka palauttavat aina tietyn arvon.
