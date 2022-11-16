from random import randint
from random import choice


class Arpa:
    """Satunnaisuudet"""
    def arvo_kokonaisluku(self, a, b):
        """ Arvotaan kokonaisluku kahden luvun väliltä """
        return randint(a, b)

    def arvo_joukosta(self, alkiot):
        """ Arvotaan jokin joukossa esiintyvä alkio """
        valinta = None
        try:
            valinta = choice(list(alkiot))
        except IndexError as error:
            print(error)
        except TypeError as error:
            print(error)
        return valinta
