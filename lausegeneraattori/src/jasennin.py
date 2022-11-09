class Jasennin:

    """
    Erottaa välimerkit (.,!?) sanoista, ja tallentaa jokaisen
    sanan ja välimerkin omaksi alkiokseen listaan

    Parametrit:
        teksti: Merkkijono jota käsitellään

    Palauttaa listan sanoista ja välimerkeistä
    """

    def jasenna_listaksi(self, teksti):
        jasennetty = teksti.replace(
            "\n", " ").replace(
                ".", " . ").replace(
                    ",", " , ").replace(
                        "!", " ! ").replace(
                            "?", " ? ").split()

        return jasennetty
