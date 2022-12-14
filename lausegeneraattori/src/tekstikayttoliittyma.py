import os
from konsoli import Konsoli
from tiedostonlukija import TiedostonLukija
from ohjelma import Ohjelma


class TekstiKayttoliittyma:
    """ Pääohjelma """

    def __init__(self,
        konsoli: "Konsoli",
        tiedostonlukija: "TiedostonLukija",
        ohjelma: "Ohjelma"
    ):
        """
        Konstruktori

        Parametrit:
            konsoli: tulostukseen ja syötteiden lukuun
            tiedostonlukija: Palauttaa tiedoston sisällön merkkijonona
            ohjelma: ohjelma jonka kanssa käyttöliittymä kommunikoi
        """
        self._ohjelma = ohjelma
        self._tiedostonlukija = tiedostonlukija
        self._konsoli = konsoli

    def _paavalikon_ohjeet(self):
        self._konsoli.kirjoita("1: valitse aste")
        self._konsoli.kirjoita("2: lataa tiedosto")
        self._konsoli.kirjoita("3: muodosta lause")
        self._konsoli.kirjoita("4: muodosta tarina")
        self._konsoli.kirjoita("t: trien koko")
        self._konsoli.kirjoita("q: lopeta")
        self._konsoli.kirjoita("h: päävalikon vaihtoehdot")

    def kaynnista(self):
        """
        Pääsilmukka

        Pyydetään käyttäjältä syötettä ja toimitaan sen mukaisesti.
        """
        self._paavalikon_ohjeet()

        while True:
            syote = self._konsoli.lue("toiminto: ")
            if syote == "1":
                self._valitse_aste()
            elif syote == "2":
                self._valitse_tiedosto()
            elif syote == "3":
                self._lauseen_alku()
            elif syote == "4":
                self._tarinan_alku()
            elif syote == "h":
                self._paavalikon_ohjeet()
            elif syote == "t":
                self._konsoli.kirjoita(
                    self._ohjelma.hae_trien_koko()
                )
            elif syote == "q":
                break
        self._konsoli.kirjoita("suljetaan ohjelma")

    def _valitse_aste(self):
        """ Uuden asteen valinta """
        self._konsoli.kirjoita(f"nykyinen aste: {self._ohjelma.hae_aste()}")
        syote = self._konsoli.lue("syötä uusi aste (pos. kokonaisluku): ")

        tulos = self._ohjelma.vaihda_aste(syote)
        if tulos:
            self._konsoli.kirjoita("aste vaihdttu, tiedostot ladattava uudestaan")
        else:
            self._konsoli.kirjoita("astetta ei vaihdettu")

    def _valitse_tiedosto(self):
        """
        Ladataan tiedosto, jonka sisältö luetaan ja annetaan
        ohjelmalle
        """
        sisalto = ""
        syote = self._konsoli.lue("tiedoston nimi: ")
        if syote == "KAIKKI":
            polku = os.path.join(os.path.dirname(__file__), "data")
            tiedosto_lista = self._tiedostonlukija.kaikkien_tiedostojen_nimet(polku)
            for tiedoston_nimi in tiedosto_lista:
                sisalto = self._tiedostonlukija.lue(os.path.join(polku, tiedoston_nimi))
                if len(sisalto) > 0:
                    self._ohjelma.lataa_tiedoston_sisalto(sisalto)
                    self._konsoli.kirjoita(os.path.join(polku, tiedoston_nimi))
        else:
            polku = os.path.join(os.path.dirname(__file__), "data", syote)
            sisalto = self._tiedostonlukija.lue(polku)
            if len(sisalto) > 0:
                self._ohjelma.lataa_tiedoston_sisalto(sisalto)
                self._konsoli.kirjoita(os.path.join(polku))

    def _lauseen_alku(self):
        """
        Lähetetään ohjelmalle lauseen alku tai tyhjä
        merkkijono
        """
        alku = self._konsoli.lue("Alkusanat: ")
        lause = self._ohjelma.lauseen_muodostuksen_aloitus(alku)
        if lause:
            self._konsoli.kirjoita(lause)
        else:
            self._konsoli.kirjoita("Virhe. Muista ladata tiedosto(ja)")

    def _tarinan_alku(self):
        """
        Kirjoitetaan alku tarinalle, ja luodaan tarina niiden pohjalta.
        Tyhjäksi jättäminen arpoo ensimmäisen sanan.

        """
        pituus = self._konsoli.lue("pituus sanoina: ")
        try:
            pituus = int(pituus)
        except ValueError as error:
            self._konsoli.kirjoita(error)
            return

        alku = self._konsoli.lue("Alkusanat: ")
        tarina = self._ohjelma.tarinan_muodostuksen_aloitus(alku, pituus)
        if tarina:
            self._konsoli.kirjoita(tarina)
        else:
            self._konsoli.kirjoita("Virhe. Muista ladata tiedosto(ja)")
