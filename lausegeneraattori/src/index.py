import os.path
from tietorakenteet.trie import Trie
from konsoli import Konsoli
from tiedostonlukija import TiedostonLukija
from arpa import Arpa


def paavalikon_ohjeet():
    print("1: valitse aste")
    print("2: lisää kansiosta 'data' tiedoston sisältö")
    print("3: tuota lause!")
    print("q: lopeta")


def pilko_syotettava_data_asteen_mukaisesti(data, aste):
    """ Pilkotaan data listoihin asteen mukaan """
    lista = []
    aste = aste + 1
    if aste > len(data):
        print("asteen oltava pienempi kuin syötteen pituus")
        return False

    for i in range(len(data) - aste + 1):
        sisalista = []
        kohta = i
        while kohta < i + aste and kohta < len(data):
            print(data[kohta])
            sisalista.append(data[kohta])
            kohta += 1
        lista.append(sisalista)
        print()
    return lista

def laheta_trielle(trie, lista):
    pass

def ohjelma():
    io = Konsoli()
    tiedoston_lukija = TiedostonLukija()
    trie = Trie(Arpa())
    aste = 2
    paavalikon_ohjeet()

    while True:
        syote = io.lue("toiminto: ")

        if syote == "1":
            uusi_aste = io.lue("Aseta uusi aste (tiedostot ladattava uudestaan): ")
            try:
                uusi_aste_numerona = int(uusi_aste)
                if uusi_aste_numerona >= 0:
                    aste = uusi_aste_numerona
            except:
                io.kirjoita("Syötä vain positiivisia kokonaislukuja tai 0")
                continue
        elif syote == "2":
            print(tiedoston_lukija.lue("dracula.txt"))
        elif syote == "3":
            io.kirjoita("lause")
        elif syote == "q":
            break
        elif syote == "t":
            trie.syvyyspuu()
        else:
            pilko_syotettava_data_asteen_mukaisesti(
                [1, 2, 3, 4 ,5],
                aste
            )
            paavalikon_ohjeet()

if __name__ == "__main__":
    ohjelma()