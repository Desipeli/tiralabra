import os.path
from os import listdir


class TiedostonLukija:

    def lue(self, tiedoston_nimi):
        """
        Ohjelmalle syötettävän tiedoston lukeminen

        Parametrit:
            tiedosto: data-kansiossa olevan tiedoston nimi

        Palauttaa tiedoston sisällön merkkijonona

        """
        sisalto = ""
        try:
            with open(
                os.path.dirname(__file__)+"/data/"+tiedoston_nimi,
                "r",
                encoding="UTF-8") as tiedosto:

                sisalto = tiedosto.read()
        except FileNotFoundError as error:
            print(error)
        except IsADirectoryError as error:
            print(error)

        return sisalto

    def kaikkien_tiedostojen_nimet(self):
        """Palautetaan kaikkien tiedostojen nimet"""
        return listdir(os.path.dirname(__file__)+"/data/")
