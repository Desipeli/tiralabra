# Testausdokumentti

[Suorituskyky](#Suorituskyky)

## Yksikkötestaus

Yksikkötestit on suoritettu [unittest](https://docs.python.org/3/library/unittest.html) kirjaston avulla, ja testikattavuusraportti saadaan [coveragella](https://coverage.readthedocs.io/en/6.5.0/). Testit ovat sijoitettuna aina testattavien luokkien hakemistossa oleviin tests-kansioihin.
Testattavia luokkia ovat Trie, TrieSolmu, Jasennin ja Ohjelma. Käyttöliittymää ja satunnaistoimintoihin tarkoitettua Arpa-luokkaa ei testata.

Linux-ympäristössä testit voidaan suorittaa asennuksen jälkeen komennolla `poetry run invoke testcov`, jonka jälkeen testikattavuusraportti tallentuu kohteeseen `lausegeneraattori/htmlcov/index.html`. 

Viikon 3 testikattavuus: ![kuva](https://raw.githubusercontent.com/Desipeli/tiralabra/main/dokumentaatio/coverage_report_viikko_3.PNG)

## Luokkakohtaiset tiedot

### TrieSolmu

TrieSolmu testaus tapahtuu Trien testauksen välityksellä.

### Trie

Trieä testataan syöttämällä sille erilaisia 0-3 sanan listoja, joista se muodostaa solmuja. Testeillä varmistetaan, että Trie osaa luoda tarvittaessa uuden solmun, ja että uutta solmua ei luoda jos sille ei ole tarvetta. Oikeellisuus varmistetaan tarkastelemalla Trieä mm. syvyyshaulla.

Myös sanan valitsemista Triestä testataan erilaisten tilanteiden varalta, kuten:
- Mitä saadaan jos haetaan sanaa tyhjästä Triestä
- Toimiiko haku eri syvyyksillä
- Mitä jos yritetään hakea Trien syvyyttä syvemmältä
- Toimiiko isolla kirjaimella alkavan sanan hakeminen oikein

Koska sanan haku perustuu joissain tilanteissa satunnaisuuteen, on testejä varten luotu luokat `StubArpa1` ja `StubArpa2`, jotka palauttavat aina tietyn arvon.

### Jasennin (jäsennin)

Testataan, että Jasennin muodostaa tekstistä listoja ja listoista tekstejä oikein. Erityisesti on keskitytty välimerkkien(,.!?) testaamiseen, sillä ne käyttäytyvät hieman eri lailla kuin "normaalit" sanat.

### Ohjelma

Pääohjelman testaus on enimmäkseen integraatiotestausta. Siinä testataan, että esimerkiksi ohjelmalle syötetty merkkijono "tiedosto" tallentuu Trieen ja sen pohjalta voidaan muodostaa lauseita. Taas on pyritty huomioimaan erikoistapauksia, kuten tyhjän "tiedoston" tallentaminen, väärän muotoisen syötteen antaminen yms.

## Suorituskyky

### Jäsennin

- Tiedostosta luetun tekstin muuttaminen listaksi, sekä merkkien ``,.!?"'--»`` erottelu tai hylkääminen: Seuraavassa kuvaajasta nähdään, että jäsennykseen kuluva aika riippuu sanojen määrän lisäksi tiedoston sisällöstä. Aikaa tähän operaatioon kuluu ohjelman toiminnan kannalta kuitenkin mitättömän vähän, alle 0.05 s.
![Jäsennys listaksi](https://raw.githubusercontent.com/Desipeli/tiralabra/main/dokumentaatio/jasennys_listaksi.png)


### Trie
- Kun tekstitiedoston sisältö on muutettu listaksi sanoja ja merkkejä, pilkotaan saatu lista asteen pituisiin listoihin jotka tallennetaan trieen. Seuraavassa kaaviossa näkyy sekä pilkkomiseen että varsinaiseen tallentamiseen kuluva aika. Listan pilkkomisen vaikutus koko operaatioon on vähäinen, alle 0.1 sekuntia. Kaaviosta nähdään myös, että asteen kasvaessa tallentamiseen kuluva aika kasvaa lineaarisesti. Kaaviossa käytetyn tiedoston sanamäärä (sisältäen välimerkit) oli 146713.
![Tallennus Trieen](https://raw.githubusercontent.com/Desipeli/tiralabra/main/dokumentaatio/pilkkominen_trieen.png)
- Seuraavassa kahdessa kaaviossa on tallennettu useita tiedostoja trieen viisi kertaa, ja laskettu keskiarvo. Ensimmäisessä kaaviossa trie on tyhjennetty ennen jokaisen tiedoston tallennusta, kun taas toisessa ei. Tulosten vertailusta huomaa, että triestä jo löytyvien sanalistojen tallentaminen on nopeampaa kuin täysin uusien.
![Kaikkien tallennus tyhjään trieen](https://raw.githubusercontent.com/Desipeli/tiralabra/main/dokumentaatio/tallennus_trie_tyhennetaan.png)
![Kaikkien talllennus trieen](https://raw.githubusercontent.com/Desipeli/tiralabra/main/dokumentaatio/tallennus_trie_ei_tyhjenneta.png)
- Solmujen lukumäärä kasvaa lineaarisesti asteen kasvaessa:
![tilavaativuus](https://raw.githubusercontent.com/Desipeli/tiralabra/main/dokumentaatio/tilavaativuus.png)
