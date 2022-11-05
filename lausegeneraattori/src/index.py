import os.path
from trie.trie import Trie


def paavalikon_ohjeet():
    print("1: valitse aste")
    print("2: lisää kansiosta 'data' tiedoston sisätlö")
    print("3: tuota lause!")
    print("q: lopeta")

def lue_tiedosto(tiedosto):
    sisalto = open(os.path.dirname(__file__)+"/data/"+tiedosto, "r")
    parsetettu = sisalto.read().replace("\n", " ").replace(".", " .").replace(",", " ,").replace("!", " !").replace("?", " ?").split()
    print(parsetettu)

def pilko_syotettava_data_asteen_mukaisesti(data, aste):
    if aste > len(data):
        print("asteen oltava pienempi kuin syötteen pituus")
        return False

    for i in range(len(data) - aste + 1):
        kohta = i
        while kohta < i + aste and kohta < len(data):
            print(data[kohta])
            kohta += 1
        print()

def ohjelma():
    aste = 2
    paavalikon_ohjeet()

    while True:
        syote = input("toiminto: ")

        if syote == "1":
            uusi_aste = input("Aseta uusi aste (tiedostot ladattava uudestaan): ")
            try:
                uusi_aste_numerona = int(uusi_aste)
                if uusi_aste_numerona >= 0:
                    aste = uusi_aste_numerona
            except:
                print("Syötä vain positiivisia kokonaislukuja tai 0")
                continue
        elif syote == "2":
            lue_tiedosto("dracula.txt")
        elif syote == "3":
            print("lause")
        elif syote == "q":
            break
        else:
            pilko_syotettava_data_asteen_mukaisesti(
                [1, 2, 3, 4 ,5],
                aste
            )
            paavalikon_ohjeet()

if __name__ == "__main__":
    ohjelma()