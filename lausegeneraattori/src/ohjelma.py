from tietorakenteet.trie import Trie
from jasennin import Jasennin
from arpa import Arpa


class Ohjelma:
    """ Pääohjelma """

    def __init__(self,
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
        self._arpa = arpa

        self.aste = 2

    def vaihda_aste(self, uusi_aste):
        """ Uuden asteen valinta """

        try:
            uusi_aste = int(uusi_aste)
        except ValueError:
            return "Asteen oltava kokonaisluku >= 0"

        if uusi_aste < 0:
            return "Aste ei voi olla negatiivinen"
        if uusi_aste == self.aste:
            return "Astetta ei vaihdettu"

        self._trie = Trie(self._arpa)
        self.aste = uusi_aste

        return f"Uusi aste: {self.aste}, tiedostot ladattava uudestaan"

    def lataa_tiedoston_sisalto(self, sisalto: str):
        """
        Ladataan tekstiä ohjelmaan, muutetaan listaksi
        ja tallennetaan trieen.

        Parametrit:
            sisalto: merkkijono

        Palauttaa False jos sisaltöä ei ole, muuten True
        """
        if sisalto:
            lista = self._jasennin.jasenna_listaksi(sisalto)
            self._pilko_ja_laheta_trielle(lista)
            return True
        return False

    def _pilko_ja_laheta_trielle(self, data: list):
        """
        Valitaan listasta asteen pituiset sanajonot ja lähetetään ne
        trielle.

        Parametrit:
            data: lista sanoja ja välimerkkejä
        """
        aste = self.aste + 1
        if aste > len(data):
            return (False, "asteen oltava pienempi kuin syötteen pituus")
        for i in range(len(data) - aste + 1):
            sanalista = []
            dataosoitin = i
            while dataosoitin < i + aste and dataosoitin < len(data):
                sanalista.append(data[dataosoitin])
                dataosoitin += 1
            self._trie.lisaa_sanalista(sanalista)
        return True

    def lauseen_muodostuksen_aloitus(self, alku: str):
        """
        Muodostetaan lause alkusanojen perusteella. Jos funktiota
        kutsutaan tyhjällä merkkijonolla, arvotaan ensimmäiseksi sanaksi
        jokin sellainen sana, joka alkaa isolla alkukirjaimella.

        Parametrit:
            alku: tyhjä, tai sanoista koostuva merkkijono

        Palauttaa valmiin lauseen merkkijonona
        """
        if len(alku) == 0:
            alku = self._trie.hae_sana_juuresta_isolla_alkukirjaimella()
        jasennetty = self._jasennin.jasenna_listaksi(alku)
        return self._muodosta_lause_loppuun(jasennetty)

    def tarinan_muodostuksen_aloitus(self, alku: str, pituus_rajoitus: int):
        """
        Muodostetaan tarina alkusanojen perusteella. Jos funktiota
        kutsutaan tyhjällä merkkijonolla, arvotaan ensimmäiseksi sanaksi
        isolla alkukirjaimella alkava sana.

        Parametrit:
            alku: Tyhjä, tai sanoista koostuva merkkijono
            pituus_rajoitus: Kun sanojen määrä on saavuttanut tämän arvon,
                lopetetaan tekstin muodostus seuraavaan lopetusmerkkiin.

        Palauttaa vähintään pituus_rajoitus:n mittaisen tekstin

        """
        try:
            pituus_rajoitus = int(pituus_rajoitus)
        except ValueError:
            return (False, "Pituusrajoituksen oltava kokonaisluku")

        if len(alku) == 0:
            alku = self._trie.hae_sana_juuresta_isolla_alkukirjaimella()
        lista_sanoja = self._jasennin.jasenna_listaksi(alku)
        tekstin_pituus = len(alku)

        while True:
            if tekstin_pituus >= pituus_rajoitus:
                return self._muodosta_lause_loppuun(lista_sanoja)
            sana = None
            if self.aste == 0:
                sana = self._trie.hae([])
            else:
                sana = self._uusi_sana_edellisten_perusteella(lista_sanoja[-self.aste : ])
            lista_sanoja.append(sana)
            tekstin_pituus += 1

    def _muodosta_lause_loppuun(self, teksti: list):
        """
        Haetaan tekstiin niin kauan uusia sanoja, kunnes
        vastaan tulee jokin lopetusmerkki.

        Parametrit:
            teksti: merkkijono

        Palauttaa tekstin, joka päättyy lopetusmerkkiin.
        """
        lopetusmerkit = [".","!","?"]

        while True:
            sana = None
            if self.aste == 0:
                sana = self._arpa.arvo_joukosta(lopetusmerkit)
            else:
                sana = self._uusi_sana_edellisten_perusteella(teksti[-self.aste : ])
            teksti.append(sana)
            if sana in lopetusmerkit:
                break

        return self._jasennin.jasenna_tekstiksi(teksti)

    def _uusi_sana_edellisten_perusteella(self, viimeiset_sanat: list):
        """
        Haetaan uusi sana listalla olevien sanojen perusteella

        Kokeillaan ensin kaikilla. Jos ei löydy, tiputetaan ensimmäinen
        pois ja kokeillaan uudestaan.

        Parametrit:
            viimeiset_sanat: listan muodossa n viimeistä sanaa
        """

        sana = self._trie.hae(viimeiset_sanat)
        if not sana:
            return self._uusi_sana_edellisten_perusteella(viimeiset_sanat[1:])
        return sana
