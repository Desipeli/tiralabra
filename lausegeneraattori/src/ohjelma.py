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

        self._aste = 2

    def _paavalikon_ohjeet(self):
        self._konsoli.kirjoita("1: valitse aste")
        self._konsoli.kirjoita("2: lataa tiedosto")
        self._konsoli.kirjoita("3: muodosta lause")
        self._konsoli.kirjoita("4: muodosta tarina")
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
                self._valitse_tiedosto()
            elif syote == "3":
                self._lauseen_alku()
            elif syote == "4":
                self._tarinan_alku()
            elif syote == "t":
                self._konsoli.kirjoita(self._trie.syvyyspuu())
                self._konsoli.kirjoita(len(self._trie.syvyyspuu()))
            elif syote == "h":
                self._paavalikon_ohjeet()
            elif syote == "q":
                break
        self._konsoli.kirjoita("suljetaan ohjelma")

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

    def _valitse_tiedosto(self):
        """
        Ladataan tiedosto, jonka sisältö jäsennetään ja lisätään
        trieen.
        """
        tiedoston_nimi = self._konsoli.lue("tiedoston nimi: ")
        if tiedoston_nimi == "KAIKKI":
            tiedosto_lista = self._tiedostonlukija.kaikkien_tiedostojen_nimet()
            for tiedosto in tiedosto_lista:
                self._lataa_tiedosto(tiedosto)
        else:
            self._lataa_tiedosto(tiedoston_nimi)

    def _lataa_tiedosto(self, tiedoston_nimi):
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

    def _lauseen_alku(self):
        """
        Annetaan alku lauseelle, jonka jälkeen ohjelma
        kirjoittaa sen loppuun. Tyhjäksi jättäminen arpoo
        ensimmäisen sanan
        """
        alku = self._konsoli.lue("Alkusanat: ")
        if len(alku) == 0:
            alku = self._trie.hae_sana_juuresta_isolla_alkukirjaimella()
        alku = self._jasennin.jasenna_listaksi(alku)
        self._muodosta_lause_loppuun(alku)
        self._konsoli.kirjoita(
            self._jasennin.jasenna_tekstiksi(alku))

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
        if len(alku) == 0:
            alku = self._trie.hae_sana_juuresta_isolla_alkukirjaimella()
        alku = self._jasennin.jasenna_listaksi(alku)
        self._muodosta_tekstia(alku, pituus)

    def _muodosta_tekstia(self, alku, pituus_rajoitus):
        """
        Tekstin muodostus

        Lopetetaan kun teksti on tarpeeksi pitkä ja se loppuu
        johonkin merkeistä ,.!?

        """
        lista_sanoja = alku
        tekstin_pituus = len(alku)

        while True:
            if tekstin_pituus >= pituus_rajoitus:
                self._muodosta_lause_loppuun(lista_sanoja)
                break
            sana = None
            if self._aste == 0:
                sana = self._trie.hae([])
            else:
                sana = self._uusi_sana_edellisten_perusteella(lista_sanoja[-self._aste : ])
            lista_sanoja.append(sana)
            tekstin_pituus += 1

        self._konsoli.kirjoita(
            self._jasennin.jasenna_tekstiksi(lista_sanoja))

    def _muodosta_lause_loppuun(self, tekstin_alku):
        lopetusmerkit = [".","!","?"]

        while True:
            sana = None
            if self._aste == 0:
                sana = self._arpa.arvo_joukosta(lopetusmerkit)
            else:
                sana = self._uusi_sana_edellisten_perusteella(tekstin_alku[-self._aste : ])
            tekstin_alku.append(sana)
            if sana in lopetusmerkit:
                break


    def _uusi_sana_edellisten_perusteella(self, viimeiset_sanat):
        """
        Kokeillaan ensin kaikilla. Jos ei löydy, tiputetaan ensimmäinen
        pois ja kokeillaan uudestaan.

        Parametrit:
            viimeiset_sanat: listan muodossa n viimeistä sanaa
        """

        sana = self._trie.hae(viimeiset_sanat)
        if not sana:
            return self._uusi_sana_edellisten_perusteella(viimeiset_sanat[1:])
        return sana
