import sys
from tietorakenteet.trie import Trie
from konsoli import Konsoli
from tiedostonlukija import TiedostonLukija
from jasennin import Jasennin
from arpa import Arpa
from ohjelma import Ohjelma
from tekstikayttoliittyma import TekstiKayttoliittyma
from gui import GUI
from tests.suorituskykytestaus import SuoritusTestaus
from gutenberg_lukija import GutenbergLukija



if __name__ == "__main__":
    arpa = Arpa()
    konsoli = Konsoli()
    tiedostonlukija = TiedostonLukija()
    jasennin = Jasennin()
    gutenberg_lukija = GutenbergLukija("https://www.gutenberg.org/browse/languages/fi")
    ohjelma = Ohjelma(jasennin, arpa)

    if len(sys.argv) == 2:
        if sys.argv[1] == "teksti":
            TekstiKayttoliittyma(
                konsoli,
                tiedostonlukija,
                ohjelma
            ).kaynnista()
        elif sys.argv[1] == "test":
            SuoritusTestaus()
        sys.exit(0)
    GUI(ohjelma, tiedostonlukija, konsoli, gutenberg_lukija)
