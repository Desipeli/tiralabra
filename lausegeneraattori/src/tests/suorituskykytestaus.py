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

        tulokset = self.kaikkien_tiedostojen_tallennus_tyhjaan_trieen(tiedostot, 1)
        self.kaikki_tyhjaan_trieen_kuvaaja(tulokset)

        tulokset = self.kaikkien_tiedostojen_tallennus_trieen(tiedostot, 1)
        self.kaikki_trieen_kuvaaja(tulokset)

        tulokset = self.tekstin_jasennys_listaksi(tiedostot)
        self.teksti_listaksi_kuvaaja(tulokset)

    def kaikkien_tiedostojen_tallennus_tyhjaan_trieen(self, tiedostot: list, aste: int, toistot: int = 5):
        """
        Tallennetaan kaikki suoraan data-hakemiston alla olevat tiedostot trieen siten,
        että trie tyhjennetään aina välissä.

        Parametrit:
            tiedostot: Tiedostojen nimet
            aste: aste jolla tiedostojen sisältö tallennetaan
            toistot: kuinka monta kertaa operaatio tehdään. Lopuksi tallennetaan keskiarvo
        """
        tulokset = []
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
            tulokset.append((tiedosto, sanoja, aikojen_summa / toistot))
        return tulokset

    def kaikkien_tiedostojen_tallennus_trieen(self, tiedostot: list, aste: int, toistot: int = 5):
        """
        Kuin ylempi funktio, mutta trieä ei tyhjennetä välissä.
        """
        tulokset = {}
        self.ohjelma.vaihda_aste(aste)
        for toisto in range(toistot):
            t = tiedostot.copy()
            for tiedosto in range(len(tiedostot)):
                tiedosto = random.choice(t)
                if tiedosto not in tulokset:
                    tulokset[tiedosto] = (0,0)
                t.remove(tiedosto)
                polku = os.path.join(self.datapolku, tiedosto)
                sisalto = self.tiedostonlukija.lue(polku)
                sanoja = len(Jasennin().jasenna_listaksi(sisalto))
                alku = time()
                self.ohjelma.lataa_tiedoston_sisalto(sisalto)
                tulokset[tiedosto] = (
                    tulokset[tiedosto][0] + time() - alku,
                    sanoja)
            print("KAIKKI", toisto, tulokset)
        for avain, arvo in tulokset.items():
            tulokset[avain] = (arvo[0] / toistot, arvo[1])
        return tulokset

    def tekstin_jasennys_listaksi(self, tiedostot: list):
        """ jäsennetään teksti listaksi """
        tulokset = []
        for tiedosto in tiedostot:
            sisalto = self.tiedostonlukija.lue(os.path.join(self.datapolku, tiedosto))
            alku = time()
            lista = Jasennin().jasenna_listaksi(sisalto)
            tulokset.append((tiedosto, time()-alku, len(lista)))
        return tulokset

    def teksti_listaksi_kuvaaja(self, tulokset):
        """
        Kuvaaja näyttää, miten sanojen määrä vaikuttaa tiedoston
        sisällön jäsentämiseen
        
        """
        tapaukset = sorted(tulokset, key=lambda a: a[2])
        x = [x[2] for x in tapaukset]
        y = [y[1] for y in tapaukset]

        plt.plot(x, y, label = "Jäsennys")

        plt.xlabel("Sanojen määrä (mukana myös merkit: ,.!"+'"'+",)")
        plt.ylabel("Aika (s)")
        plt.title("Syötteenä olevan tekstin muuttaminen listaksi")
        plt.legend()
        plt.show()

    def kaikki_tyhjaan_trieen_kuvaaja(self, tulokset):
        """
        Kuvaaja tyhjään trieen tallentamisesta
        """
        tulokset = sorted(tulokset, key= lambda a: a[1])
        print("Aika yhteensä:", sum([x[2] for x in tulokset]))
        x = [x[1] for x in tulokset]
        y = [y[2] for y in tulokset]
        plt.plot(x, y)
        plt.xlabel("Sanojen lkm")
        plt.ylabel("Aika (s)")
        plt.title("Tallennukseen kuluva aika, kun trie on tyhjä")
        plt.show()

    def kaikki_trieen_kuvaaja(self, tulokset):
        """
        Kuvaaja trieen tallentamisesta, kun sitä ei tyhjennetä välissä
        """
        tulokset = tulokset.values()
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