class Jasennin:

    def jasenna_listaksi(self, teksti: str) -> list:
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
                            "'", "").replace(
                                '"', "").replace(
                                    "»", "").replace(
                                        "--", "").replace(
                                            "?", " ? ").split()

        return jasennetty

    def jasenna_tekstiksi(self, lista: list) -> str:
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
            )

        return jasennetty

    def poista_gutenberg(self, sanat: list) -> list:
        """
        Päätellään *** esiintymisien perusteella alku ja loppu.
        Joissain kirjoissa *** on kiinni sanassa, joten tarkastettava sisältyykö
        se millään tavalla sanaan.
        """
        tahtia = 0
        lopullinen_lista_sanoja = []
        for sana in sanat:
            if "***" in sana:
                tahtia += 1
                continue
            if tahtia > 2:
                break
            if tahtia == 2:
                lopullinen_lista_sanoja.append(sana)
        return lopullinen_lista_sanoja
