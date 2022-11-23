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
            jasennin: datan muuttaminen sopivaan muotoon
            arpa: satunnaislukugeneraattori
        """
        self._trie = Trie(arpa)
        self._jasennin = jasennin
        self._arpa = arpa

        self._aste = 2

    def hae_aste(self):
        return self._aste

    def vaihda_aste(self, uusi_aste):
        """ Uuden asteen valinta """

        try:
            uusi_aste = int(uusi_aste)
        except ValueError:
            return False

        if uusi_aste < 0:
            return False
        if uusi_aste == self._aste:
            return False

        self._trie = Trie(self._arpa)
        self._aste = uusi_aste

        return True

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
            return self._pilko_ja_laheta_trielle(lista)
        return False

    def _pilko_ja_laheta_trielle(self, data: list):
        """
        Valitaan listasta kaikki peräkkäiset asteen pituiset
        sanajonot ja lähetetään ne trielle.

        Parametrit:
            data: lista sanoja ja välimerkkejä
        """
        aste = self._aste
        if aste >= len(data):
            return False

        for i in range(len(data) - aste):
            sanalista = []
            dataosoitin = i
            while dataosoitin < i + aste + 1 and dataosoitin < len(data):
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
        if self.hae_trien_koko() == 0:
            return False

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
            return False

        if self.hae_trien_koko() == 0:
            return False

        if len(alku) == 0:
            alku = self._trie.hae_sana_juuresta_isolla_alkukirjaimella()
        lista_sanoja = self._jasennin.jasenna_listaksi(alku)

        tekstin_pituus = len(lista_sanoja)
        while True:
            if tekstin_pituus >= pituus_rajoitus:
                return self._muodosta_lause_loppuun(lista_sanoja)
            sana = None
            if self._aste == 0:
                sana = self._trie.hae([])
            else:
                sana = self._uusi_sana_edellisten_perusteella(lista_sanoja[-self._aste : ])
            lista_sanoja.append(sana)
            tekstin_pituus += 1

    def _muodosta_lause_loppuun(self, teksti: list):
        """
        Haetaan tekstiin niin kauan uusia sanoja, kunnes
        vastaan tulee jokin lopetusmerkki. Katkaisin määrittää
        maksimi määrän sanoja, jonka jälkeen uusien sanojen lisääminen
        viimeistään lopetetaan

        Parametrit:
            teksti: merkkijono

        Palauttaa tekstin, joka päättyy lopetusmerkkiin.
        """
        lopetusmerkit = [".","!","?"]
        katkaisin = 20

        while True:
            sana = None
            if self._aste == 0 or katkaisin == 0:
                sana = self._arpa.arvo_joukosta(lopetusmerkit)
            else:
                sana = self._uusi_sana_edellisten_perusteella(teksti[-self._aste : ])
            teksti.append(sana)
            if sana in lopetusmerkit:
                break
            katkaisin -= 1

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

    def hae_trien_koko(self):
        return len(self._trie.syvyyspuu())
