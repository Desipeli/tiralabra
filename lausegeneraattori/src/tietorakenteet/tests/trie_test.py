import unittest
from tietorakenteet.trie import Trie

class StubArpa1:
    def arvo_kokonaisluku(self, a, b):
        return 1

    def arvo_joukosta(self, joukko):
        if len(joukko) == 0:
            return None
        lista = list(joukko)
        return lista[0]

class StubArpa2:
    def arvo_kokonaisluku(self, a, b):
        return 2

    def arvo_joukosta(self, joukko):
        print(joukko)
        if len(joukko) == 0:
            return None
        lista = list(joukko)
        return lista[1]

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
        self.assertEqual(loydetty_sana, "sana")

    def test_hae_sana_juuren_alta_1_vaihtoehto2(self):
        self.trie.lisaa_sanalista(["sana"])
        self.trie.lisaa_sanalista(["sana"])

        loydetty_sana = self.trie.hae([])
        self.assertEqual(loydetty_sana, "sana")

    def test_hae_sana_juuren_alta_vaihtoehtoja(self):
        self.trie.lisaa_sanalista(["sana"])
        self.trie.lisaa_sanalista(["toinen"])
        self.trie.lisaa_sanalista(["kolmas"])

        loydetty_sana = self.trie.hae([])
        self.assertEqual(loydetty_sana, "sana")

    def test_hae_sana_juuren_alta_toinen_vaihtoehto(self):
        self.trie2.lisaa_sanalista(["sana"])
        self.trie2.lisaa_sanalista(["toinen"])
        self.trie2.lisaa_sanalista(["kolmas"])

        loydetty_sana = self.trie2.hae([])
        self.assertEqual(loydetty_sana, "toinen")

    def test_hae_sana_toiselta_tasolta_1_vaihtoehto(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi", "kolme"])

        loydetty_sana = self.trie.hae(["yksi"])
        self.assertEqual(loydetty_sana, "kaksi")

    def test_hae_sana_toiselta_tasolta_1_vaihtoehto2(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi", "kolme"])
        self.trie.lisaa_sanalista(["yksi", "kaksi", "kolme"])

        loydetty_sana = self.trie.hae(["yksi"])
        self.assertEqual(loydetty_sana, "kaksi")

    def test_hae_sana_toiselta_tasolta_vaihtoehtoja(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi"])
        self.trie.lisaa_sanalista(["yksi", "kolme"])

        loydetty_sana = self.trie.hae(["yksi"])
        self.assertEqual(loydetty_sana, "kaksi")

    def test_hae_sana_toiselta_tasolta_vaihtoehtoja2(self):
        self.trie2.lisaa_sanalista(["yksi", "kaksi"])
        self.trie2.lisaa_sanalista(["yksi", "kolme"])

        loydetty_sana = self.trie2.hae(["yksi"])
        self.assertEqual(loydetty_sana, "kolme")

    def test_haku_tyhjaan_trien_juureen(self):
        loydetty_sana = self.trie.hae([])

        self.assertEqual(None, loydetty_sana)

    def test_haku_solmuun_jolla_ei_ole_lapsia(self):
        self.trie.lisaa_sanalista(["yksi", "kaksi"])
        loydetty_sana = self.trie.hae(["yksi", "kaksi"])

        self.assertEqual(loydetty_sana, None)

    def test_haku_solmuun_jolla_ei_ole_lapsia_ja_listaa_on_viela_jaljella(self):
        self.trie.lisaa_sanalista(["yksi"])
        loydetty_sana = self.trie.hae(["yksi", "kaksi"])

        self.assertEqual(loydetty_sana, None)

    # Hae sana joka alkaa isolla alkukirjaimella

    def test_haku_iso_alkukirjain_tyhja_trie(self):
        sana = self.trie.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, None)

    def test_haku_iso_alkukirjain_yksi_pienlla_alkava_sana_juuressa(self):
        self.trie.lisaa_sanalista(["sana"])
        sana = self.trie.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, "sana")

    def test_haku_iso_alkukirjain_monta_pienella_alkavaa_sanaa_juuressa(self):
        self.trie.lisaa_sanalista(["yksi"])
        self.trie.lisaa_sanalista(["kaksi"])
        self.trie.lisaa_sanalista(["kolme"])

        sana = self.trie.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertAlmostEqual(sana, "yksi")

    def test_haku_iso_alkukirjain_monta_pienella_alkavaa_sanaa_juuressa2(self):
        self.trie2.lisaa_sanalista(["yksi"])
        self.trie2.lisaa_sanalista(["kaksi"])
        self.trie2.lisaa_sanalista(["kolme"])
        sana = self.trie2.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, "kaksi")

    def test_haku_iso_alkukirjain_1_isolla_alkava_sana_juuressa(self):
        self.trie.lisaa_sanalista(["Sana"])
        sana = self.trie.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, "Sana")

    def test_haku_iso_alkukirjain_monta_isolla_alkavaa_sanaa_juuressa(self):
        self.trie.lisaa_sanalista(["Yksi"])
        self.trie.lisaa_sanalista(["Kaksi"])
        self.trie.lisaa_sanalista(["Kolme"])
        sana = self.trie.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, "Yksi")

    def test_haku_iso_alkukirjain_monta_isolla_alkavaa_sanaa_juuressa2(self):
        self.trie2.lisaa_sanalista(["Yksi"])
        self.trie2.lisaa_sanalista(["Kaksi"])
        self.trie2.lisaa_sanalista(["Kolme"])
        sana = self.trie2.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, "Kaksi")

    def test_haku_iso_alkukirjain_valitusta_seuraava_on_iso(self):
        self.trie.lisaa_sanalista(["yksi"])
        self.trie.lisaa_sanalista(["Kaksi"])
        self.trie.lisaa_sanalista(["kolme"])
        sana = self.trie.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, "Kaksi")

    def test_haku_iso_alkukirjain_valitusta_edellinen_on_iso(self):
        self.trie2.lisaa_sanalista(["Yksi"])
        self.trie2.lisaa_sanalista(["kaksi"])
        self.trie2.lisaa_sanalista(["kolme"])
        sana = self.trie2.hae_sana_juuresta_isolla_alkukirjaimella()

        self.assertEqual(sana, "Yksi")
