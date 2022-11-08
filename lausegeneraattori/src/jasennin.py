class Jasennin:

    def jasenna_listaksi(self, teksti):
        jasennetty = teksti.replace(
            "\n", " ").replace(
                ".", " . ").replace(
                    ",", " , ").replace(
                        "!", " ! ").replace(
                            "?", " ? ").split()

        return jasennetty
