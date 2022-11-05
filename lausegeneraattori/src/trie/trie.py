from .trie_solmu import TrieSolmu

class Trie:
    """ Trie-tietorakenne"""
    
    def __init__(self) -> None:
        """ Konstruktori. Luodaan juurisolmu """

        self.root = TrieSolmu("")
    
    def lisaa_sanalista(self, sanalista: list):
        """ 
        Sijoitetaan annettu lista sanoja trieen

        Kutsutaan lisaa_sana funktiota, aloitetaan juuresta.
        
        Parametrit:
            sanalista: lista

        """

        solmu = self.root
        self._lisaa_sana(sanalista, solmu)
    
    def _lisaa_sana(self, sanalista: list, solmu: "TrieSolmu"):
        sana = sanalista.pop(0)
        
        if sana in solmu.lapset:
            """ kasvatetaan arvoa ja siirrytään solmuun """
            solmu.lukumaara += 1
            solmu = solmu.lapset[sana]
        else:
            """ Luodaan solmu ja siirrytään siihen """
            uusi_solmu = TrieSolmu(sana)
            solmu.lapset[sana] = uusi_solmu
            solmu = uusi_solmu
        
        if len(sanalista) > 0:
            self._lisaa_sana(sanalista, solmu)
        return
    
    def tulosta_puu_syvyys(self):
        solmu = self.root

        for s in solmu.lapset.values():
            print(s)
            self._tulosta_solmu_syvyys(s)

    def _tulosta_solmu_syvyys(self, solmu):

        for s in solmu.lapset.values():
            print(s)
            self._tulosta_solmu_syvyys(s)
