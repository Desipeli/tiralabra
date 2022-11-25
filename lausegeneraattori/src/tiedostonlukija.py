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
                tiedoston_nimi,
                "r",
                encoding="UTF-8") as tiedosto:

                sisalto = tiedosto.read()
        except FileNotFoundError as error:
            print(error)
        except IsADirectoryError as error:
            print(error)

        return sisalto

    def kaikkien_tiedostojen_nimet(self, hakemisto):
        """Palautetaan kaikkien .txt-päätteisten tiedostojen nimet"""
        tiedostolista = listdir(hakemisto)
        return [nimi for nimi in tiedostolista if len(nimi) >= 4 and nimi[-4:] == ".txt"]
