import unittest
from jasennin import Jasennin


class TestJasennin(unittest.TestCase):
    def setUp(self) -> None:
        self.jasennin = Jasennin()

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
