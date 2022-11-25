import os
import random
from time import time, sleep
import matplotlib.pyplot as plt
from ohjelma import Ohjelma
from arpa import Arpa
from jasennin import Jasennin
from tiedostonlukija import TiedostonLukija
from tietorakenteet.trie import Trie


class SuoritusTestaus:
    """
    Ohjelman suorituskyvyn testaus
    
    Testaukseen käytettävät tiedostot haetaan suoraan data-kansion alta
    """

    def __init__(self):
        """ Konstruktori """
        self.ohjelma = Ohjelma(Jasennin(), Arpa())
        self.tiedostonlukija = TiedostonLukija()
        self.datapolku = os.path.join(os.path.dirname(__file__), "../data")
        tiedostot = self.tiedostonlukija.kaikkien_tiedostojen_nimet(self.datapolku)
        self.alusta_tulokset(tiedostot)

        tr1 = os.path.join(self.datapolku, "taistelu_roomasta_1.txt")

        self.tekstin_jasennys_listaksi(tiedostot)

        for i in range(6):
            print("tallennetaan", tr1, "asteella", i)
            self.laske_trieen_talletusaika(tr1, i)

        for avain, arvo in self.tulokset.items():
            print(avain)
            print(arvo)
            print()
            
        self.trieen_tallennuksen_kuvaaja()
        self.teksti_listaksi_kuvaaja()

    def alusta_tulokset(self, tiedostot):
        self.tulokset = {}
        self.tulokset["tiedostoja"] = len(tiedostot)
        self.tulokset["jasennykset"] = []
        self.tulokset["trieen"] = []



    def tekstin_jasennys_listaksi(self, tiedostot: list):
        """ jäsennetään teksti listaksi """
        for tiedosto in tiedostot:
            sisalto = self.tiedostonlukija.lue(os.path.join(self.datapolku, tiedosto))
            alku = time()
            lista = Jasennin().jasenna_listaksi(sisalto)
            self.tulokset["jasennykset"].append((tiedosto, time()-alku, len(lista)))

    def laske_trieen_talletusaika(self, tiedosto, aste):
        sisalto = TiedostonLukija().lue(tiedosto)
        sanat_listana = Jasennin().jasenna_listaksi(sisalto)
        self.pilko_ja_laheta_trielle_aika(sanat_listana, aste)

    def pilko_ja_laheta_trielle_aika(self, data: list, aste: int):
        """
        Ohjelmasta kopioitu trieen tallennusfunktio. Tehdään yhdelle tiedostolle
        """
        trie = Trie(Arpa())

        if aste >= len(data):
            return False
        aika_sanalista = 0
        aika_trie = 0
        for i in range(len(data) - aste):
            alku_sanalista = time()
            sanalista = []
            dataosoitin = i
            while dataosoitin < i + aste + 1 and dataosoitin < len(data):
                sanalista.append(data[dataosoitin])
                dataosoitin += 1
            aika_sanalista += time() - alku_sanalista
            alku_trie = time()
            trie.lisaa_sanalista(sanalista)
            aika_trie += time() - alku_trie

        self.tulokset["trieen"].append((aste, aika_sanalista, aika_trie))
        print("sanlistojen muodostukseen kulunut aika", aika_trie)
        print("Trieen talletusten aika", aika_sanalista)
        return True

    def teksti_listaksi_kuvaaja(self):
        tapaukset = sorted(self.tulokset["jasennykset"], key=lambda a: a[2])
        print("tapaukset", tapaukset)
        x = [x[2] for x in tapaukset]
        y = [y[1] for y in tapaukset]

        plt.plot(x, y, label = "Jäsennys")

        plt.xlabel("Sanojen määrä (mukana myös merkit: ,.!"+'"'+",)")
        plt.ylabel("Aika (s)")
        plt.title("Syötteenä olevan tekstin muuttaminen listaksi")
        plt.legend()
        plt.show()

    def trieen_tallennuksen_kuvaaja(self):
        print(self.tulokset["trieen"])

        x = [x[0] for x in self.tulokset["trieen"]]
        y = [y[1] for y in self.tulokset["trieen"]]
        plt.plot(x, y, label = "Pilkkominen")
        plt.xlabel("Aste")
        plt.ylabel("Aika (s)")

        x = [x[0] for x in self.tulokset["trieen"]]
        y = [y[2] for y in self.tulokset["trieen"]]
        plt.plot(x, y, label = "Trieen")

        x = [x[0] for x in self.tulokset["trieen"]]
        y = [y[1]+y[2] for y in self.tulokset["trieen"]]
        plt.plot(x, y, label="Yhteensä")

        plt.xticks(range(len(self.tulokset["trieen"])))
        plt.title(
        "Tiedoston sanoista koostuvan listan pilkkominen asteen mittaisiin \nlistoihin ja niiden tallentaminen Trieen")
        plt.legend()
        plt.show()
if __name__ == "__main__":
    testaus = SuoritusTestaus()