from tietorakenteet.trie import Trie
from konsoli import Konsoli
from tiedostonlukija import TiedostonLukija
from jasennin import Jasennin
from arpa import Arpa


class Ohjelma:
    """ Pääohjelma """

    def __init__(self,
        konsoli: "Konsoli",
        tiedostonlukija: "TiedostonLukija",
        jasennin: "Jasennin",
        arpa: "Arpa"
    ):
        """
        Konstruktori

        Parametrit:
            konsoli: tulostukseen ja syötteiden lukuun
            tiedostonlukija: Palauttaa tiedoston sisällön merkkijonona
            jasennin: datan muuttaminen sopivaan muotoon
            arpa: satunnaislukugeneraattori
        """
        self._trie = Trie(arpa)
        self._jasennin = jasennin
        self._tiedostonlukija = tiedostonlukija
        self._konsoli = konsoli
        self._arpa = arpa

        self._aste = 0

    def _paavalikon_ohjeet(self):
        self._konsoli.kirjoita("1: valitse aste")
        self._konsoli.kirjoita("2: lataa tiedosto")
        self._konsoli.kirjoita("3: tulosta lause")
        self._konsoli.kirjoita("q: lopeta")
        self._konsoli.kirjoita("t: tulosta trie")
        self._konsoli.kirjoita("h: päävalikon vaihtoehdot")

    def kaynnista(self):
        """
        Ohjelman pääsilmukka

        Pyydetään käyttäjältä syötettä ja toimitaan sen mukaisesti.
        """
        self._paavalikon_ohjeet()

        while True:
            syote = self._konsoli.lue("toiminto: ")
            if syote == "1":
                self._valitse_aste()
            elif syote == "2":
                self._lataa_tiedosto()
            elif syote == "3":
                self._konsoli.kirjoita("lause")
            elif syote == "t":
                self._konsoli.kirjoita(self._trie.syvyyspuu())
                self._konsoli.kirjoita(len(self._trie.syvyyspuu()))
            elif syote == "h":
                self._paavalikon_ohjeet()
            elif syote == "q":
                break

    def _valitse_aste(self):
        """ Uuden asteen valinta """
        self._konsoli.kirjoita(f"nykyinen aste: {self._aste}")
        syote = self._konsoli.lue("syötä uusi aste (pos. kokonaisluku): ")

        try:
            syote = int(syote)
        except ValueError:
            self._konsoli.kirjoita("virhe: syötteen oltava kokonaisluku")
            self._konsoli.kirjoita("astetta ei vaihdettu")
            return

        if syote < 0 or syote == self._aste:
            self._konsoli.kirjoita("astetta ei vaihdettu")
        else:
            self._trie = Trie(self._arpa)
            self._aste = syote
            self._konsoli.kirjoita(f"aste vaihdettu: {self._aste}")
            self._konsoli.kirjoita("syötteet ladattava uudestaan")

    def _lataa_tiedosto(self):
        """
        Ladataan tiedosto, jonka sisältö jäsennetään ja lisätään
        trieen.
        """
        tiedoston_nimi = self._konsoli.lue("tiedoston nimi: ")
        sisalto = self._tiedostonlukija.lue(tiedoston_nimi)
        if sisalto:
            lista = self._jasennin.jasenna_listaksi(sisalto)
            self._pilko_ja_laheta_trielle(lista)
            self._konsoli.kirjoita(f"{tiedoston_nimi} ladattu")

    def _pilko_ja_laheta_trielle(self, data):
        """
        Valitaan listasta aseen pituiset sanajonot ja lähetetään ne
        trielle.

        Parametrit:
            data: lista sanoja ja välimerkkejä
        """
        aste = self._aste + 1
        if aste > len(data):
            self._konsoli.kirjoita("asteen oltava pienempi kuin syötteen pituus")
            return
        for i in range(len(data) - aste + 1):
            sanalista = []
            dataosoitin = i
            while dataosoitin < i + aste and dataosoitin < len(data):
                sanalista.append(data[dataosoitin])
                dataosoitin += 1
            self._trie.lisaa_sanalista(sanalista)
