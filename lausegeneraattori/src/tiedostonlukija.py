import os.path


class TiedostonLukija:
    """
    Ohjelmalle syötettävän tiedoston lukeminen

    Parametrit:
        tiedosto: data-kansiossa olevan tiedoston nimi

    Palauttaa tiedoston sisällön merkkijonona

    """

    def lue(self, tiedosto):
        sisalto = open(os.path.dirname(__file__)+"/data/"+tiedosto,
        "r",
        encoding="UTF-8").read()

        return sisalto
