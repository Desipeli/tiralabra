class Tulosteet:
    """ Ohjelman tulosteet """
    def paavalikko(self):
        return [
            "1: valitse aste",
            "2: lataa tiedosto", 
            "3: muodosta lause",
            "4: muodosta tarina",
            "q: lopeta",
            "t: tulosta trie",
            "h: päävalikon vaihtoehdot"
        ]

    def sulje(self):
        return ["suljetaan ohjelma"]