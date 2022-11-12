class Konsoli:
    """
    Syötteiden lukeminen ja tulostaminen

    Tarkoitus helpottaa integraatiotestaamista
    """
    def lue(self, teksti):
        return input(teksti)

    def kirjoita(self, teksti):
        print(teksti)
