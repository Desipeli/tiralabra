import unittest
from jasennin import Jasennin
from ohjelma import Ohjelma
from tests.tulosteet import Tulosteet
from tests.stubs import StubArpa1, StubArpa2, StubKonsoli, StubTiedostonlukija
from tests.stubs import Tiedostot


class TestOhjelma(unittest.TestCase):
    def setUp(self):
        self.jasennin = Jasennin()
        self.arpa_1 = StubArpa1()
        self.arpa_2 = StubArpa2()
        self.tulosteet = Tulosteet()
        self.tiedostot = Tiedostot()
        # self.konsoli = StubKonsoli()
        # self.tiedostonlukija = StubTiedostonlukija()

    def test_ohjelman_voi_sammuttaa(self):
        konsoli = StubKonsoli(["q"])
        print("syötteet aluksi", konsoli.syotteet)
        ohjelma = Ohjelma(
            konsoli,
            StubTiedostonlukija([]),
            self.jasennin,
            self.arpa_1
            )

        ohjelma.kaynnista()

        self.assertListEqual(konsoli.syotteet, [])
        self.assertListEqual(konsoli.kirjoitetut,
            self.tulosteet.paavalikko() + self.tulosteet.sulje()
            )

    # Aste

    def test_aste_on_aluksi_2_ja_asteen_voi_vaihtaa_0(self):
        konsoli = StubKonsoli(["1", "0", "q"])
        print("syötteet aluksi", konsoli.syotteet)
        ohjelma = Ohjelma(
            konsoli,
            StubTiedostonlukija([]),
            self.jasennin,
            self.arpa_1
            )

        ohjelma.kaynnista()
        print(konsoli.kirjoitetut)
        self.assertListEqual(konsoli.kirjoitetut,
            self.tulosteet.paavalikko() + [
            "nykyinen aste: 2",
            "aste vaihdettu: 0",
            "syötteet ladattava uudestaan"
            ] + self.tulosteet.sulje()
        )

    def test_astetta_ei_voi_vaihtaa_negatiiviseksi(self):
        konsoli = StubKonsoli(["1", "-2", "q"])
        print("syötteet aluksi", konsoli.syotteet)
        ohjelma = Ohjelma(
            konsoli,
            StubTiedostonlukija([]),
            self.jasennin,
            self.arpa_1
            )

        ohjelma.kaynnista()
        print(konsoli.kirjoitetut)
        self.assertListEqual(konsoli.kirjoitetut,
            self.tulosteet.paavalikko() + [
            "nykyinen aste: 2",
            "astetta ei vaihdettu"
            ] + self.tulosteet.sulje()
        )

    def test_asteen_vaihtaminen_samaksi_ei_muuta_astetta(self):
        konsoli = StubKonsoli(["1", "2", "q"])
        print("syötteet aluksi", konsoli.syotteet)
        ohjelma = Ohjelma(
            konsoli,
            StubTiedostonlukija([]),
            self.jasennin,
            self.arpa_1
            )

        ohjelma.kaynnista()
        print(konsoli.kirjoitetut)
        self.assertListEqual(konsoli.kirjoitetut,
            self.tulosteet.paavalikko() + [
            "nykyinen aste: 2",
            "astetta ei vaihdettu"
            ] + self.tulosteet.sulje()
        )

    def test_