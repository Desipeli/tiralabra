import unittest
from jasennin import Jasennin


class TestJasennin(unittest.TestCase):
    def setUp(self) -> None:
        self.jasennin = Jasennin()

    # Teksti listaksi

    def test_jasenna_tyhja_merkkijono(self):
        jasennetty = self.jasennin.jasenna_listaksi("")

        self.assertAlmostEqual(jasennetty, [])

    def test_jasenna_simppelia_tekstia(self):
        jasennetty = self.jasennin.jasenna_listaksi(
            "Olipa kerran synkkä ja myrskyinen yö"
            )

        self.assertAlmostEqual(jasennetty,
            ["Olipa", "kerran", "synkkä", "ja", "myrskyinen", "yö"]
        )

    def test_pilkku_lauseessa(self):
        jasennetty = self.jasennin.jasenna_listaksi(
            "Suo, kuokka ja Jussi"
        )

        self.assertAlmostEqual(jasennetty,
            ["Suo", ",", "kuokka", "ja", "Jussi"]
        )

    def test_piste_lauseessa(self):
        jasennetty = self.jasennin.jasenna_listaksi(
            "Piste. Ja toinen."
        )

        self.assertAlmostEqual(jasennetty,
            ["Piste", ".", "Ja", "toinen", "."]
        )

    def test_huutomerkki_lauseessa(self):
        jasennetty = self.jasennin.jasenna_listaksi(
            "Hihii! Hehee!"
        )

        self.assertAlmostEqual(jasennetty,
            ["Hihii", "!", "Hehee", "!"]
        )

    def test_kysymysmerkki_lauseessa(self):
        jasennetty = self.jasennin.jasenna_listaksi(
            "Kuka? Mikä?"
        )

        self.assertAlmostEqual(jasennetty,
            ["Kuka", "?", "Mikä", "?"]
        )

    def test_liikaa_valilyonteja(self):
        jasennetty = self.jasennin.jasenna_listaksi(
            "   Juu,  joo o  "
        )

        self.assertAlmostEqual(jasennetty,
            ["Juu", ",", "joo", "o"]
        )

    def test_mielivaltainen_merkkijono(self):
        jasennetty = self.jasennin.jasenna_listaksi(
            "  .?aaa..,o?o "
        )

        self.assertAlmostEqual(jasennetty,
            [".", "?", "aaa", ".", ".", ",", "o", "?", "o"]
        )

    # Lista tekstiksi

    def test_tekstiksi_tyhja_lista(self):
        jasennetty = self.jasennin.jasenna_tekstiksi([])

        self.assertAlmostEqual(jasennetty, "")

    def test_tekstiksi_yksi_sana(self):
        jasennetty = self.jasennin.jasenna_tekstiksi(["sana"])

        self.assertAlmostEqual(jasennetty, "sana")

    def test_tekstiksi_monta_sanaa(self):
        jasennetty = self.jasennin.jasenna_tekstiksi(
            ["Olipa", "kerran", "synkkä", "ja"]
        )

        self.assertAlmostEqual(jasennetty, "Olipa kerran synkkä ja")

    def test_tekstiksi_sanoja_ja_valimerkkeja(self):
        jasennetty = self.jasennin.jasenna_tekstiksi(
            ["!", "jaa", "?", "?", "juu", ","]
        )

        self.assertAlmostEqual(jasennetty, "! jaa?? juu,")

    # Gutenberg

    def test_poista_gutenberg_ennen_tekstia(self):
        jasennetty = self.jasennin.poista_gutenberg(
            ["moi", "hei", "***", "START", "of...", "***", "juu, joo, jaa"]
        )
        self.assertEqual(jasennetty, ["juu, joo, jaa"])

    def test_poista_gutenberg_jalkeen_tekstin(self):
        jasennetty = self.jasennin.poista_gutenberg(
            ["***", "***", "moi", "***", "hei"]
        )
        self.assertEqual(jasennetty, ["moi"])