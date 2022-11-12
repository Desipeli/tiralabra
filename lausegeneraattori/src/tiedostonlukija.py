import os.path


class TiedostonLukija:
    """
    Ohjelmalle syötettävän tiedoston lukeminen

    Parametrit:
        tiedosto: data-kansiossa olevan tiedoston nimi

    Palauttaa tiedoston sisällön merkkijonona

    """

    def lue(self, tiedoston_nimi):
        sisalto = ""
        try:
            with open(
                os.path.dirname(__file__)+"/data/"+tiedoston_nimi,
                "r",
                encoding="UTF-8") as tiedosto:

                sisalto = tiedosto.read()
        except FileNotFoundError as error:
            print(error)

        return sisalto
