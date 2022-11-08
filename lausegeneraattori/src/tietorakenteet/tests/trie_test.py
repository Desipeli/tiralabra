import unittest
from tietorakenteet.trie import Trie

class StubArpa1:
    def arvo(self, a, b):
        return 1

class StubArpa2:
    def arvo(self, a, b):
        return 2

class TestTrie(unittest.TestCase):
    def setUp(self) -> None:

        self.trie = Trie(StubArpa1())
        self.trie2 = Trie(StubArpa2())

    # Ensin yhdellä sanalistalla

    def test_tyhja_trie_ei_tulosta_mitaan(self):
        tulos = self.trie.syvyyspuu()

        self.assertListEqual(tulos, [])

    def test_lisataan_yksittainen_sana(self):
        self.trie.lisaa_sanalista(["sana"])

        syvyyspuu = self.trie.syvyyspuu()
        arvot = [str(x) for x in syvyyspuu]
        self.assertListEqual(arvot, ["sana 1"])

    def test_lisataan_monta_erilaista_sanaa_yksi_lista(self):
        self.trie.lisaa_sanalista(
            ["yksi", "kaksi", "kolme"]
        )

        syvyyspuu = self.trie.syvyyspuu()
        arvot = [str(x) for x in syvyyspuu]
        self.assertListEqual(
            arvot,
            ["yksi 1", "kaksi 1", "kolme 1"]
        )

    def test_lisataan_monta_samanlaista_sanaa_yksi_lista(self):
        self.trie.lisaa_sanalista(
            ["yksi","yksi","yksi"]
        )

        syvyyspuu = self.trie.syvyyspuu()
        arvot = [str(x) for x in syvyyspuu]
        self.assertListEqual(
            arvot,
            ["yksi 1", "yksi 1", "yksi 1"]
        )

    # Useammalla sanalistalla

    def test_monta_sanalistaa_eri_sanat(self):
        self.trie.lisaa_sanalista(
            ["yksi", "kaksi", "kolme"]
        )
        self.trie.lisaa_sanalista(
            ["neljä", "viisi", "kuusi"]
        )

        syvyyspuu = self.trie.syvyyspuu()
        arvot = [str(x) for x in syvyyspuu]
        self.assertListEqual(
            arvot,
            ["yksi 1", "kaksi 1", "kolme 1",
            "neljä 1", "viisi 1", "kuusi 1"]
        )

    def test_monta_sanalistaa_samoja_sanoja(self):
        self.trie.lisaa_sanalista(
            ["yksi", "kaksi", "kolme"]
        )
        self.trie.lisaa_sanalista(
            ["yksi", "kaksi", "neljä"]
        )

        syvyyspuu = self.trie.syvyyspuu()
        arvot = [str(x) for x in syvyyspuu]
        self.assertListEqual(
            arvot,
            ["yksi 2", "kaksi 2", "kolme 1", "neljä 1"]
        )

    # Hakutoiminto

    def test_hae_sana_juuren_alta_1_vaihtoehto(self):
        self.trie.lisaa_sanalista(["sana"])

        loydetty_sana = self.trie.hae([])
        self.assertAlmostEqual(loydetty_sana, "sana")

    def test_hae_sana_juuren_alta_1_vaihtoehto2(self):
        self.trie.lisaa_sanalista(["sana"])
        self.trie.lisaa_sanalista(["sana"])

        loydetty_sana = self.trie.hae([])
        self.assertAlmostEqual(loydetty_sana, "sana")

    def test_hae_sana_juuren_alta_vaihtoehtoja(self):
        self.trie.lisaa_sanalista(["sana"])
        self.trie.lisaa_sanalista(["toinen"])
        self.trie.lisaa_sanalista(["kolmas"])

        loydetty_sana = self.trie.hae([])
        self.assertAlmostEqual(loydetty_sana, "sana")

    def test_hae_sana_juuren_alta_toinen_vaihtoehto(self):
        self.trie2.lisaa_sanalista(["sana"])
        self.trie2.lisaa_sanalista(["toinen"])
        self.trie2.lisaa_sanalista(["kolmas"])

        loydetty_sana = self.trie2.hae([])
        self.assertAlmostEqual(loydetty_sana, "toinen")

    def test_hae_sana_toiselta_tasolta_1_vaihtoehto(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi", "kolme"])

        loydetty_sana = self.trie.hae(["yksi"])
        self.assertAlmostEqual(loydetty_sana, "kaksi")

    def test_hae_sana_toiselta_tasolta_1_vaihtoehto2(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi", "kolme"])
        self.trie.lisaa_sanalista(["yksi", "kaksi", "kolme"])

        loydetty_sana = self.trie.hae(["yksi"])
        self.assertAlmostEqual(loydetty_sana, "kaksi")

    def test_hae_sana_toiselta_tasolta_vaihtoehtoja(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi"])
        self.trie.lisaa_sanalista(["yksi", "kolme"])

        loydetty_sana = self.trie.hae(["yksi"])
        self.assertAlmostEqual(loydetty_sana, "kaksi")

    def test_hae_sana_toiselta_tasolta_vaihtoehtoja2(self):
        self.trie2.lisaa_sanalista(["yksi", "kaksi"])
        self.trie2.lisaa_sanalista(["yksi", "kolme"])

        loydetty_sana = self.trie2.hae(["yksi"])
        self.assertAlmostEqual(loydetty_sana, "kolme")

    def test_haku_tyhjaan_trien_juureen(self):
        loydetty_sana = self.trie.hae([])

        self.assertAlmostEqual(None, loydetty_sana)

    def test_haku_solmuun_jolla_ei_ole_lapsia(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi"])
        loydetty_sana = self.trie.hae(["yksi", "kaksi"])

        self.assertAlmostEqual(loydetty_sana, None)

    def test_haku_solmuun_jolla_ei_ole_lapsia_ja_listaa_on_viela_jaljella(self):
        self.trie.lisaa_sanalista(["yksi"])
        loydetty_sana = self.trie.hae(["yksi", "kaksi"])

        self.assertAlmostEqual(loydetty_sana, None)
