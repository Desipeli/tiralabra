import unittest
from jasennin import Jasennin
from ohjelma import Ohjelma

class StubArpa1:
    def arvo_kokonaisluku(self, a, b):
        return 1

    def arvo_joukosta(self, joukko):
        if len(joukko) == 0:
            return None
        lista = list(joukko)
        return lista[0]

class TestOhjelma(unittest.TestCase):
    def setUp(self):
        self.ohjelma = Ohjelma(Jasennin(), StubArpa1())

    # Aste

    def test_aste_on_aluksi_2(self):
        self.assertAlmostEqual(2, self.ohjelma.hae_aste())

    def test_asteen_vaihto_0(self):
        palaute = self.ohjelma.vaihda_aste(0)
        self.assertAlmostEqual(palaute, True)
        self.assertAlmostEqual(self.ohjelma.hae_aste(), 0)

    def test_asteen_vaihto_neg(self):
        aste_ennen = self.ohjelma.hae_aste()
        palaute = self.ohjelma.vaihda_aste(-1)
        self.assertAlmostEqual(palaute, False)
        self.assertAlmostEqual(self.ohjelma.hae_aste(), aste_ennen)

    def test_asteen_vaihto_epakelpo_merkkijono(self):
        aste_ennen = self.ohjelma.hae_aste()
        palaute = self.ohjelma.vaihda_aste("moikkelis")
        self.assertAlmostEqual(palaute, False)
        self.assertAlmostEqual(self.ohjelma.hae_aste(), aste_ennen)

    # Trieen tallennus

    def test_tyhjan_merkkijonon_tallennus_trieen(self):
        palaute = self.ohjelma.lataa_tiedoston_sisalto("")
        self.assertAlmostEqual(palaute, False)
        self.assertAlmostEqual(self.ohjelma.hae_trien_koko(), 0)

    def test_sanoista_koostuvan_merkkijonon_tallennus_trieen_aste_0(self):
        self.ohjelma.vaihda_aste(0)
        palaute = self.ohjelma.lataa_tiedoston_sisalto(
            "Olipa kerran tarina"
        )
        self.assertAlmostEqual(palaute, True)
        self.assertAlmostEqual(self.ohjelma.hae_trien_koko(), 3)

    def test_valimerkkien_tallennus_trieen(self):
        self.ohjelma.vaihda_aste(0)
        palaute = self.ohjelma.lataa_tiedoston_sisalto(
            "Yks! Kaks? Kolme, neljä ja viisi."
        )
        self.assertAlmostEqual(palaute, True)
        self.assertAlmostEqual(self.ohjelma.hae_trien_koko(), 10)

    def test_lyhyen_merkkijonon_tallennus_trieen_aste_2(self):
        self.ohjelma.vaihda_aste(2)
        palaute = self.ohjelma.lataa_tiedoston_sisalto(
            "Olipa kerran tarina"
        )
        self.assertAlmostEqual(palaute, True)
        self.assertAlmostEqual(self.ohjelma.hae_trien_koko(), 3)

    def test_pitkan_merkkijonon_tallennus_trieen_aste_2(self):
        self.ohjelma.vaihda_aste(2)
        palaute = self.ohjelma.lataa_tiedoston_sisalto(
            "Olipa kerran tarina, joka jatkui ja jatkui ja jatkui"
        )
        self.assertAlmostEqual(palaute, True)
        self.assertAlmostEqual(self.ohjelma.hae_trien_koko(), 21)

    def test_tallennettava_merkkijono_yhtasuuri_kuin_aste(self):
        self.ohjelma.vaihda_aste(2)
        palaute = self.ohjelma.lataa_tiedoston_sisalto("Hei vaan")
        self.assertAlmostEqual(palaute, False)
        self.assertAlmostEqual(self.ohjelma.hae_trien_koko(), 0)

    def test_tallennettava_merkkijono_lyhyempi_kuin_aste(self):
        self.ohjelma.vaihda_aste(2)
        palaute = self.ohjelma.lataa_tiedoston_sisalto("Hei")
        self.assertAlmostEqual(palaute, False)
        self.assertAlmostEqual(self.ohjelma.hae_trien_koko(), 0)

    # Lauseen muodostus

    def test_lause_kun_trie_tyhja_alku_tyhja(self):
        lause = self.ohjelma.lauseen_muodostuksen_aloitus("")
        self.assertAlmostEqual(lause, False)

    def test_lause_kun_trie_tyhja_alku_ei_tyhja(self):
        lause = self.ohjelma.lauseen_muodostuksen_aloitus("Nelkku kelkku")
        self.assertAlmostEqual(lause, False)

    def test_lause_triessa_pienella_alkavia_sanoja_tyhja_alku_aste_0(self):
        self.ohjelma.vaihda_aste(0)
        self.ohjelma.lataa_tiedoston_sisalto("yks kaks kolme")
        lause = self.ohjelma.lauseen_muodostuksen_aloitus("")
        self.assertAlmostEqual(lause, "yks.")

    def test_lause_triessa_pienella_alkavia_on_alku_aste_0(self):
        self.ohjelma.vaihda_aste(0)
        self.ohjelma.lataa_tiedoston_sisalto("yks kaks kolme")
        lause = self.ohjelma.lauseen_muodostuksen_aloitus("Olipa kerran")
        self.assertAlmostEqual(lause, "Olipa kerran.")

    def test_lause_triessa_ei_lopetusmerkkeja_aste_2(self):
        self.ohjelma.vaihda_aste(2)
        self.ohjelma.lataa_tiedoston_sisalto("yks kaks kolme")
        lause = self.ohjelma.lauseen_muodostuksen_aloitus("Olipa kerran")
        print(lause)
        self.assertAlmostEqual(lause,
            "Olipa kerran yks kaks kolme yks kaks kolme yks kaks kolme yks "
            + "kaks kolme yks kaks kolme yks kaks kolme yks kaks."
        )

    def test_lause_triessa_pienella_alkavia_ja_lopetusmerkkeja_aste_2(self):
        self.ohjelma.vaihda_aste(2)
        self.ohjelma.lataa_tiedoston_sisalto(". olipa kerra, vai oliko?")
        lause = self.ohjelma.lauseen_muodostuksen_aloitus("hii huu")
        print(lause)
        self.assertAlmostEqual(lause, "hii huu.")

    # Tarina

    def test_tarina_trie_tyhja(self):
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus("", 3)
        self.assertAlmostEqual(tarina, False)

    def test_tarina_trie_tyhja_on_alku(self):
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus("", 3)
        self.assertAlmostEqual(tarina, False)

    def test_tarina_ei_alkua_aste_2_pituus_0(self):
        self.ohjelma.vaihda_aste(2)
        self.ohjelma.lataa_tiedoston_sisalto("yks kaks kolme")
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus("", 0)
        print(tarina)
        self.assertAlmostEqual(tarina,
            "yks kaks kolme yks kaks kolme yks kaks kolme yks "
            +"kaks kolme yks kaks kolme yks kaks kolme yks kaks kolme."
        )

    def test_tarina_ei_alkua_aste_2_pituus_0_juuressa_isolla_alkavia(self):
        self.ohjelma.vaihda_aste(2)
        self.ohjelma.lataa_tiedoston_sisalto("yks kaks Kolme")
        self.ohjelma.lataa_tiedoston_sisalto("Kolme kaks Kolme")
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus("", 1)
        print(tarina)
        self.assertAlmostEqual(tarina,
            "Kolme kaks Kolme kaks Kolme kaks Kolme kaks Kolme kaks "
            +"Kolme kaks Kolme kaks Kolme kaks Kolme kaks Kolme kaks Kolme."
        )

    def test_tarina_epakelpo_pituus(self):
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus("", "pöö")
        self.assertAlmostEqual(tarina, False)

    def test_tarina_on_alku(self):
        self.ohjelma.vaihda_aste(2)
        self.ohjelma.lataa_tiedoston_sisalto(". yks kaks kolme")
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus(". yks kaks", 0)
        self.assertAlmostEqual(tarina, ". yks kaks kolme.")

    def test_tarina_on_alku_pituus_rajoitus_isompi_kuin_teksin_pituus(self):
        self.ohjelma.vaihda_aste(2)
        self.ohjelma.lataa_tiedoston_sisalto(". yks kaks kolme")
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus("yks kaks", 5)
        print(tarina)
        self.assertAlmostEqual(tarina, "yks kaks kolme. yks kaks kolme.")

    def test_tarina_on_alku_pituus_rajoitus_isompi_teksin_pituus_aste_0(self):
        self.ohjelma.vaihda_aste(0)
        self.ohjelma.lataa_tiedoston_sisalto(". yks kaks kolme")
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus("yks kaks", 5)
        print(tarina)
        self.assertAlmostEqual(tarina, "yks kaks....")
