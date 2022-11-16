from string import punctuation
from .trie_solmu import TrieSolmu


class Trie:
    """ Trie-tietorakenne"""

    def __init__(self, arpa) -> None:
        """
        Konstruktori, luodaan juurisolmu.

        Parametrit:
            arpa: satunnaislukugeneraattori

        """
        self._arpa = arpa
        self.root = TrieSolmu("")

    def lisaa_sanalista(self, sanalista: list):
        """
        Sijoitetaan annettu lista sanoja trieen

        Kutsutaan lisaa_sana funktiota, aloitetaan juuresta.

        Parametrit:
            sanalista: lisättävät sanat listan muodossa

        """

        solmu = self.root
        self._lisaa_sana(sanalista, solmu, 0)

    def _lisaa_sana(self, sanalista: list, solmu: "TrieSolmu", syvyys: int):
        """
        Lisätään sana trieen

        Jos sanaa ei löydy kyseisen solmun lapsista, luodaan uusi.
        Jos sana löytyy, kasvatetaan sen solmun muuttujaa lukumaara yhdellä.
        Lopuksi kutsutaan rekursiivisesti samaa funktiota uudella solmulla ja syvyys +1

        Parametrit:
            sanalista: lisättävät sanat listana
            solmu: Tarkastelussa oleva solmu
            syvyys: Kuinka syvällä puussa ollaan. 0 = juuri

        """
        sana = sanalista[syvyys]

        if sana in solmu.lapset.keys():
            solmu.lapset[sana].lukumaara += 1
            uusi_solmu = solmu.lapset[sana]
        else:
            uusi_solmu = TrieSolmu(sana)
            solmu.lapset[sana] = uusi_solmu

        solmu.lapsien_lukumaara += 1

        uusi_syvyys = syvyys + 1
        if uusi_syvyys < len(sanalista):
            self._lisaa_sana(sanalista, uusi_solmu, uusi_syvyys)
        else:
            return

    def hae(self, sanalista):
        """
        Haetaan triestä sana

        Parametrit:
            sanalista: lista sanoja, joiden perusteella valitaan uusi sana

        Palauttaa sanan tai arvon None
        """

        loydetty_solmu = self._etsi_seuraava_sana(sanalista, self.root , 0)
        if loydetty_solmu:
            return loydetty_solmu.sana
        return None

    def _etsi_seuraava_sana(self, sanalista: list, solmu: "TrieSolmu", syvyys: int):
        """
        Etsiään triestä seuraava sanalistassa esiintyvä sana

        Parametrit:
            sanalista: lista sanoja
            solmu: TrieSolmu josta etsitään
            syvyys: indeksi sanalistaan

        Palauttaa:
            None: jos lapsisolmuista ei löydy haluttua sanaa
            uuden sanan, jos sellainen löydetään.
        """

        if syvyys == len(sanalista):
            return self._arvo_solmu(solmu)
        sana = sanalista[syvyys]
        if sana in solmu.lapset.keys():
            uusi_solmu = solmu.lapset[sana]
        else:
            return None

        uusi_syvyys = syvyys + 1
        return self._etsi_seuraava_sana(sanalista, uusi_solmu, uusi_syvyys)


    def _arvo_solmu(self, solmu):
        """
        Arvotaan uusi sana esiintymistiheyden perusteella

        Parametrit:
            solmu: TrieSolmu, jonka lapsisolmuista valitaan jokin

        Palauttaa:
            None jos solmulla ei ole lapsia
            TrieSolmun, jonka sana välitetään eteepäin
        """
        arvonta = self._arpa.arvo_kokonaisluku(0, solmu.lapsien_lukumaara)
        lapikaynti = 0
        uusi_solmu = None
        for lapsisolmu in solmu.lapset.values():
            lapikaynti += lapsisolmu.lukumaara
            if lapikaynti >= arvonta:
                uusi_solmu = lapsisolmu
                break
        return uusi_solmu

    def hae_sana_juuresta_isolla_alkukirjaimella(self):
        """
        Haetaan juuresta isolla alkukirjaimella alkava sana

        Arvotaan jokin sana. Jos se on välimerkki tai alkaa
        pienellä alkukirjaimella, käydään juuren lapsisolmuja
        niin kauan läpi, että löytyy isolla kirjaimella alkava.
        Jos ei löydy, palautetaan ensimmäisenä löytynyt.

        Aloitetaan läpikäynti ensimmäiseksi valitusta sanasta.
        Jos päästään loppuun, aloitetaan alusta kunnes päästään
        taas ensimmäisenä valittuun sanaan ja palautetaan se.
        """

        valittu_sana = self._arpa.arvo_joukosta(self.root.lapset)

        if not valittu_sana:
            return None
        if valittu_sana[0].isupper():
            return valittu_sana

        aikaisemmat_sanat = []
        valittu_sana_loydetty = False
        for sana in self.root.lapset:
            if sana == valittu_sana:
                valittu_sana_loydetty = True
                aikaisemmat_sanat.append(sana)
            if valittu_sana_loydetty:
                if sana[0].isupper():
                    return sana
            else:
                aikaisemmat_sanat.append(sana)

        for sana in aikaisemmat_sanat:
            if sana[0].isupper():
                return sana

        return valittu_sana

    def syvyyspuu(self):
        """ Pyydetään trieltä syvyyspuu listana """

        solmu = self.root
        lista = []

        self._syvyys_solmu(solmu, lista)
        return lista

    def _syvyys_solmu(self, solmu, lista):

        for lapsisolmu in solmu.lapset.values():
            lista.append(lapsisolmu)
            self._syvyys_solmu(lapsisolmu, lista)
