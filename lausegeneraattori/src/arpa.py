from random import randint
from random import choice


class Arpa:
    """Satunnaisuudet"""
    def arvo_kokonaisluku(self, a, b):
        return randint(a, b)

    def arvo_joukosta(self, alkiot):
        return choice(list(alkiot))
