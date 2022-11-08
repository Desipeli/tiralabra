import os.path


class TiedostonLukija:
    """ Ohjelmalle syötettävän datan lukeminen ja jäsennys """

    def lue(self, tiedosto):
        sisalto = open(os.path.dirname(__file__)+"/data/"+tiedosto,
        "r",
        encoding="UTF-8").read()

        return self._jasenna_listaksi(sisalto)

    def _jasenna_listaksi(self, teksti):
        jasennetty = teksti.replace(
            "\n", " ").replace(
                ".", " .").replace(
                    ",", " ,").replace(
                        "!", " !").replace(
                            "?", " ?").split()

        return jasennetty