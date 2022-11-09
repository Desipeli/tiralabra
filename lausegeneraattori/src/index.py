from tietorakenteet.trie import Trie
from konsoli import Konsoli
from tiedostonlukija import TiedostonLukija
from jasennin import Jasennin
from arpa import Arpa
from ohjelma import Ohjelma


if __name__ == "__main__":

    Ohjelma(
        Konsoli(),
        TiedostonLukija(),
        Jasennin(),
        Arpa()
    ).kaynnista()