import sys
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
    ohjelma = Ohjelma(jasennin, arpa)

    print(len(sys.argv))

    if len(sys.argv) == 2:
        if sys.argv[1] == "text":
            TekstiKayttoliittyma(
                konsoli,
                tiedostonlukija,
                ohjelma
            ).kaynnista()
            sys.exit(0)
    GUI(ohjelma, tiedostonlukija)
