class TrieSolmu:
    """ Trie-puu koostuu näistä solmuista """

    def __init__(self, sana) -> None:
        """
        Konstruktori

        Solmun lapset talletetaan muodossa {sana: TrieSolmu(sana)}

        Parametrit:
            sana: merkkijono
        """

        self.lapset = {}
        self.lapsien_lukumaara = 0
        self.lukumaara = 1
        self.sana = sana

    def __repr__(self) -> str:
        return f"{self.sana} {self.lukumaara}"
