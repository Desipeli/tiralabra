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
        """ Konstruktori
        Valitaan kommentoimalla mitä testataan
        """
        self.ohjelma = Ohjelma(Jasennin(), Arpa())
        self.tiedostonlukija = TiedostonLukija()
        self.datapolku = os.path.join(os.path.dirname(__file__), "../data")
        tiedostot = self.tiedostonlukija.kaikkien_tiedostojen_nimet(self.datapolku)
        self.alusta_tulokset(tiedostot)

        #tr1 = os.path.join(self.datapolku, "taistelu_roomasta_1.txt")

        #self.tekstin_jasennys_listaksi(tiedostot)

        # for i in range(6):
        #     print("tallennetaan", tr1, "asteella", i)
        #     self.laske_trieen_talletusaika(tr1, i)
        
        self.kaikkien_tiedostojen_tallennus_tyhjaan_trieen(tiedostot, 4)
        self.kaikkien_tiedostojen_tallennus_trieen(tiedostot, 4)

        for avain, arvo in self.tulokset.items():
            print(avain)
            print(arvo)
            print()
            
        # self.trieen_tallennuksen_kuvaaja()
        # self.teksti_listaksi_kuvaaja()
        self.kaikki_tyhjaan_trieen_kuvaaja()
        self.kaikki_trieen_kuvaaja()

    def alusta_tulokset(self, tiedostot):
        """ Sanakirja johon tallennetaan testien tulokset """
        self.tulokset = {}
        self.tulokset["tiedostoja"] = len(tiedostot)
        self.tulokset["jasennykset"] = []
        self.tulokset["trieen"] = []
        self.tulokset["kaikki_tyhjaan_trieen"] = []
        self.tulokset["kaikki_trieen"] = {}

    def kaikkien_tiedostojen_tallennus_tyhjaan_trieen(self, tiedostot: list, aste: int, toistot: int = 5):
        """
        Tallennetaan kaikki suoraan data-hakemiston alla olevat tiedostot trieen siten,
        että trie tyhjennetään aina välissä.

        Parametrit:
            tiedostot: Tiedostojen nimet
            aste: aste jolla tiedostojen sisältö tallennetaan
            toistot: kuinka monta kertaa operaatio tehdään. Lopuksi tallennetaan keskiarvo
        """
        t = tiedostot.copy()
        self.ohjelma.vaihda_aste(aste)
        for i in range(len(tiedostot)):
            tiedosto = random.choice(t)
            t.remove(tiedosto)
            aikojen_summa = 0
            for toisto in range(toistot):
                self.ohjelma.tyhjenna_trie()
                polku = os.path.join(self.datapolku, tiedosto)
                sisalto = self.tiedostonlukija.lue(polku)
                sanoja = len(Jasennin().jasenna_listaksi(sisalto))
                alku = time()
                self.ohjelma.lataa_tiedoston_sisalto(sisalto)
                aikojen_summa += time() - alku
            self.tulokset["kaikki_tyhjaan_trieen"].append((tiedosto, sanoja, aikojen_summa / toistot))

    def kaikkien_tiedostojen_tallennus_trieen(self, tiedostot: list, aste: int, toistot: int = 5):
        """
        Kuin ylempi funktio, mutta trieä ei tyhjennetä välissä.
        """
        self.ohjelma.vaihda_aste(aste)
        for toisto in range(toistot):
            t = tiedostot.copy()
            for tiedosto in range(len(tiedostot)):
                tiedosto = random.choice(t)
                if tiedosto not in self.tulokset["kaikki_trieen"]:
                    self.tulokset["kaikki_trieen"][tiedosto] = (0,0)
                t.remove(tiedosto)
                polku = os.path.join(self.datapolku, tiedosto)
                sisalto = self.tiedostonlukija.lue(polku)
                sanoja = len(Jasennin().jasenna_listaksi(sisalto))
                alku = time()
                self.ohjelma.lataa_tiedoston_sisalto(sisalto)
                self.tulokset["kaikki_trieen"][tiedosto] = (
                    self.tulokset["kaikki_trieen"][tiedosto][0] + time() - alku,
                    sanoja)
            print("KAIKKI", toisto, self.tulokset["kaikki_trieen"])
        for avain, arvo in self.tulokset["kaikki_trieen"].items():
            self.tulokset["kaikki_trieen"][avain] = (arvo[0] / toistot, arvo[1])

    def tekstin_jasennys_listaksi(self, tiedostot: list):
        """ jäsennetään teksti listaksi """
        for tiedosto in tiedostot:
            sisalto = self.tiedostonlukija.lue(os.path.join(self.datapolku, tiedosto))
            alku = time()
            lista = Jasennin().jasenna_listaksi(sisalto)
            self.tulokset["jasennykset"].append((tiedosto, time()-alku, len(lista)))

    def laske_trieen_talletusaika(self, tiedosto, aste):
        """ Jäsennetään sisältö ohjelman funktiolle """
        sisalto = TiedostonLukija().lue(tiedosto)
        sanat_listana = Jasennin().jasenna_listaksi(sisalto)
        self.pilko_ja_laheta_trielle_aika(sanat_listana, aste)

    def pilko_ja_laheta_trielle_aika(self, data: list, aste: int):
        """
        Ohjelmasta kopioitu trieen tallennusfunktio.
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
        """
        Kuvaaja näyttää, miten sanojen määrä vaikuttaa tiedoston
        sisällön jäsentämiseen
        
        """
        tapaukset = sorted(self.tulokset["jasennykset"], key=lambda a: a[2])
        x = [x[2] for x in tapaukset]
        y = [y[1] for y in tapaukset]

        plt.plot(x, y, label = "Jäsennys")

        plt.xlabel("Sanojen määrä (mukana myös merkit: ,.!"+'"'+",)")
        plt.ylabel("Aika (s)")
        plt.title("Syötteenä olevan tekstin muuttaminen listaksi")
        plt.legend()
        plt.show()

    def trieen_tallennuksen_kuvaaja(self):
        """
        Kuvaajasta nähdään listan pilkkomiseen ja trieen tallentamiseen
        kuluva aika.
        """
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

    def kaikki_tyhjaan_trieen_kuvaaja(self):
        """
        Kuvaaja tyhjään trieen tallentamisesta
        """
        tulokset = sorted(self.tulokset["kaikki_tyhjaan_trieen"], key= lambda a: a[1])
        print("Aika yhteensä:", sum([x[2] for x in tulokset]))
        x = [x[1] for x in tulokset]
        y = [y[2] for y in tulokset]
        plt.plot(x, y)
        plt.xlabel("Sanojen lkm")
        plt.ylabel("Aika (s)")
        plt.title("Tallennukseen kuluva aika, kun trie on tyhjä")
        plt.show()

    def kaikki_trieen_kuvaaja(self):
        """
        Kuvaaja trieen tallentamisesta, kun sitä ei tyhjennetä välissä
        """
        tulokset = self.tulokset["kaikki_trieen"].values()
        tulokset = sorted(tulokset, key= lambda a: a[1])
        x = [x[1] for x in tulokset]
        y = [y[0] for y in tulokset]
        plt.plot(x, y)
        plt.xlabel("Sanojen lkm")
        plt.ylabel("Aika (s)")
        plt.title("Tallennukseen kuluva aika, kun trieä ei tyhjennetä")
        plt.show()


if __name__ == "__main__":
    testaus = SuoritusTestaus()