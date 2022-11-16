class Jasennin:

    def jasenna_listaksi(self, teksti: str):
        """
        Erottaa välimerkit (.,!?) sanoista, ja tallentaa jokaisen
        sanan ja välimerkin omaksi alkiokseen listaan

        Parametrit:
            teksti: Merkkijono jota käsitellään

        Palauttaa listan sanoista ja välimerkeistä
        """
        jasennetty = teksti.replace(
            "\n", " ").replace(
                ".", " . ").replace(
                    ",", " , ").replace(
                        "!", " ! ").replace(
                            "?", " ? ").split()

        return jasennetty

    def jasenna_tekstiksi(self, lista: list):
        """
        Muuttaa listan merkkijonoksi, ja poistaa välimerkkien
        edestä välilyönnin

        Parametrit:
            lista: lista sanoja ja välimerkkejä

        Palauttaa merkkijonon
        """
        jasennetty = " ".join(lista).replace(
            " .", "."
            ).replace(
                " ,", ","
            ).replace(
                " !", "!"
            ).replace(
                " ?", "?"
            ).replace(
                '"', ""
            ).replace(
                "'", ""
            )

        return jasennetty
