class StubKonsoli:
    """ Testaukseen käytettävä konsolin korvike """

    def __init__(self, syotteet: list):
        """
        Konstruktori

        Parametrit:
            syotteet: lista syötteistä, mitä ohjelmalle annetaan
        """
        self.kirjoitetut = []
        self.syotteet = syotteet
        self.syotteet.reverse()

    def lue(self, teksti): # pylint: disable=unused-argument
        """ Ohjelma lukee syötteen listalta """
        return self.syotteet.pop()

    def kirjoita(self, teksti):
        """ Ohjelma kirjoittaa listalle tulostamisen sijaan """
        self.kirjoitetut.append(teksti)

class StubTiedostonlukija:
    """ Testaukseen käytettävä tiedostonlukijan korvike """

    def __init__(self, tiedostot: object):
        """
        Konstruktori

        Parametrit:
            tiedostot: olioita, jotka ovat muodossa:
                tiedoston_nimi: sisältö merkkijonona
        """

        self._tiedostot = tiedostot

    def lue(self, tiedoston_nimi):
        return self._tiedostot[tiedoston_nimi]

    def kaikkien_tiedostojen_nimet(self):
        return list(self._tiedostot)

class StubArpa1:
    def arvo_kokonaisluku(self, a, b):
        return 1

    def arvo_joukosta(self, joukko):
        if len(joukko) == 0:
            return None
        lista = list(joukko)
        return lista[0]

class StubArpa2:
    def arvo_kokonaisluku(self, a, b):
        return 2

    def arvo_joukosta(self, joukko):
        print(joukko)
        if len(joukko) == 0:
            return None
        lista = list(joukko)
        return lista[1]

class Tiedostot:
    """
    Tiedostoja testaamista varten

    'tiedostot' ovat avain-arvopareja, muotoa nimi: sisältö merkkijonona

    """
    def tiedostot_1(self):
        return {}
    
    def tiedostot_2(self):
        return {
            "a.txt": ""
        }
    
    def tiedostot_3(self):
        return {
            "a.txt": "Olipa kerran tarina, jolla ei ollut päätä eikä häntää."
        }
