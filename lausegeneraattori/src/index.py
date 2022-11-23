from tietorakenteet.trie import Trie
from konsoli import Konsoli
from tiedostonlukija import TiedostonLukija
from jasennin import Jasennin
from arpa import Arpa
from ohjelma import Ohjelma
from tekstikayttoliittyma import TekstiKayttoliittyma
from gui import GUI


if __name__ == "__main__":
    arpa = Arpa()
    konsoli = Konsoli()
    tiedostonlukija = TiedostonLukija()
    jasennin = Jasennin()

    ohjelma = Ohjelma(
        jasennin,
        arpa
    )

    # kayttoliittyma = TekstiKayttoliittyma(
    #     konsoli,
    #     tiedostonlukija,
    #     ohjelma
    # ).kaynnista()
    kayttoliittyma = GUI(ohjelma, tiedostonlukija) 
