# Testausdokumentti

## Yksikkötestaus

Yksikkötestit on suoritettu [unittest](https://docs.python.org/3/library/unittest.html) kirjaston avulla, ja testikattavuus saadaan [coveragella](https://coverage.readthedocs.io/en/6.5.0/). 
Testattavia luokkia ovat Trie, TrieSolmu, Jasennin ja Ohjelma. Käyttöliittymää ja satunnaistoimintoihin tarkoitettua Arpa-luokkaa ei testata.

Linux-ympäristössä testit voidaan suorittaa asennuksen jälkeen komennolla `poetry run invoke testcov`, jonka jälkeen testikattavuusraportti tallentuu kohteeseen `lausegeneraattori/htmlcov/index.html`. 
