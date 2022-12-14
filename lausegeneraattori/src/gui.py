import os
from time import time
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
from ohjelma import Ohjelma
from tiedostonlukija import TiedostonLukija
from konsoli import Konsoli
from gutenberg_lukija import GutenbergLukija


class GUI:
    """ Graafinen käyttöliittymä """
    def __init__(self,
        ohjelma: "Ohjelma",
        tiedostonlukija: "TiedostonLukija",
        konsoli: "Konsoli",
        gutenberg_lukija: "GutenbergLukija"):
        """ Konstruktori

        """
        self.ohjelma = ohjelma
        self.tiedostonlukija = tiedostonlukija
        self.konsoli = konsoli
        self.gutenberg = gutenberg_lukija

        self.ikkuna = tk.Tk()
        self.ikkuna.rowconfigure(0, minsize=400, weight=1)
        self.ikkuna.columnconfigure(1, minsize=300, weight=1)
        self.ikkuna.title("Lausegeneraattori")
        self.tekstilaatikko = tk.Text(self.ikkuna)
        toimintokehys = tk.Frame(self.ikkuna, relief=tk.RAISED, bd=2)

        toimintokehys.grid(row=0, column=0, sticky="ns")
        self.tekstilaatikko.grid(row=0, column=1, sticky="nsew")

        self.luo_toimintokehyksen_osat(toimintokehys)
        self.paivita_aste(self.hae_aste())
        self.ikkuna.mainloop()

    def luo_toimintokehyksen_osat(self, toimintokehys):
        """ Luodaan ja piirretään GUI:n vasen palkki """
        nappi_lataa = tk.Button(toimintokehys,
            text="Lataa paikallisia tiedostoja",
            command=self.lataa_paikallisia_tiedostoja)
        nappi_gutenberg = tk.Button(toimintokehys,
            text="Lataa Gutenberg",
            command=self.kysy_gutenberg)
        nappi_aste = tk.Button(toimintokehys, text="Vaihda aste", command=self.vaihda_aste)
        self.teksti_aste = tk.Label(toimintokehys, text="aste: ")
        teksti_triessa_solmuja = tk.Label(toimintokehys, text="Triessä solmuja:")
        self.teksti_solmut = tk.Label(toimintokehys, text="0")
        nappi_lause = tk.Button(toimintokehys,
            text="Muodosta lause",
            command=self.muodosta_lause)
        tarinan_pituus = tk.Label(toimintokehys, text="tarinan pituus min")
        self.input_tarinan_pituus = tk.Entry(toimintokehys, text="20")
        nappi_tarina = tk.Button(toimintokehys,
            text="Muodosta tarina",
            command=self.muodosta_tarina)
        nappi_kopioi = tk.Button(toimintokehys, text="Kopioi", command=self.kopioi_teksti)
        nappi_tyhjenna = tk.Button(toimintokehys, text="Tyhjennä", command=self.tyhjenna)
        nappi_tyhjenna_trie = tk.Button(toimintokehys,
            text="Tyhjennä muisti", command=self.tyhjenna_trie)

        nappi_lataa.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        nappi_gutenberg.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.teksti_aste.grid(row=2, column=0, sticky="ew", padx=5)
        nappi_aste.grid(row=3, column=0, sticky="ew", padx=5)
        teksti_triessa_solmuja.grid(row=4, column=0, sticky="ew", padx=5)
        self.teksti_solmut.grid(row=5, column=0, sticky="ew", padx=5)
        nappi_lause.grid(row=6, column=0, sticky="ew", padx=5)
        tarinan_pituus.grid(row=7, column=0, sticky="ew", padx=5)
        self.input_tarinan_pituus.grid(row=8, column=0, sticky="ew", padx=5)
        nappi_tarina.grid(row=9, column=0, sticky="ew", padx=5)
        nappi_kopioi.grid(row=10, column=0, sticky="ew", padx=5)
        nappi_tyhjenna.grid(row=11, column=0, sticky="ew", padx=5)
        nappi_tyhjenna_trie.grid(row=12, column=0, sticky="ew", padx=5)

    def lataa_paikallisia_tiedostoja(self):
        """ Voidaan ladata monta tiedostoa kerralla """
        tiedostojen_nimet = filedialog.askopenfilenames(
            initialdir= os.path.join(os.path.dirname(__file__), "data"),
            title="valitse tiedosto(t)",
            filetypes= (("Text files",
                        "*.txt*"),
                        ("all files",
                        "*.*")))
        self.konsoli.kirjoita("Aloitetaan tiedostojen lataaminen")
        tiedostoja_ladattu = 0
        tiedostoja_yhteensa = len(tiedostojen_nimet)
        latauspalkki, latauspalkki_tausta = self.luo_latauspalkki()
        self.ikkuna.update_idletasks()
        for nimi in tiedostojen_nimet:
            self.konsoli.kirjoita(f"Ladataan tiedoston {nimi} sisältö")
            sisalto = self.tiedostonlukija.lue(nimi)
            lataus_alkaa = time()
            onnistui = self.ohjelma.lataa_tiedoston_sisalto(sisalto)
            self.konsoli.kirjoita(f"aikaa kului {time() - lataus_alkaa} s")
            if not onnistui:
                m_1 = f"Tiedostoa {nimi} ei voitu ladata."
                m_2 = " Tiedostossa on oltava vähintään aste + 1 sanaa"
                messagebox.showerror(message=m_1+m_2)
            tiedostoja_ladattu += 1
            latauspalkki["value"] = tiedostoja_ladattu / tiedostoja_yhteensa * 100
            self.ikkuna.update_idletasks()
        self.konsoli.kirjoita("Valmis")
        latauspalkki_tausta.destroy()
        self.paivita_solmut()

    def kysy_gutenberg(self):
        self.vaihda_gutenberg_url()

        maara = simpledialog.askinteger(title="Kirjojen määrä",
            prompt="Montako kirjaa ladataan?")
        if isinstance(maara, int):
            print("Aloitetaan kirjojen lataaminen")
            latauspalkki, latauspalkki_tausta = self.luo_latauspalkki()
            self.gutenberg.sekoita_kirjalista()
            latauspalkki["value"] = 0 / maara * 100
            self.ikkuna.update_idletasks()
            for i in range(1, maara + 1):
                print(i)
                if self.gutenberg.kirjalistan_koko() == 0:
                    print("Ei enempää kirjoja")
                    break
                self.hae_gutenberg()
                self.paivita_solmut()
                latauspalkki["value"] = i / maara * 100
                self.ikkuna.update_idletasks()
            latauspalkki_tausta.destroy()
            print("Valmis")

    def hae_gutenberg(self):
        kirja = self.gutenberg.hae_kirja()
        if not kirja:
            return False
        return self.ohjelma.lataa_tiedoston_sisalto(kirja)

    def vaihda_gutenberg_url(self):
        url = simpledialog.askstring(title="Mistä ladataan?",
            prompt="Esim. https://www.gutenberg.org/browse/languages/fi")
        if url:
            self.gutenberg.aseta_url(url)
            self.gutenberg.hae_linkit()

    def luo_latauspalkki(self):
        latauspalkki_tausta = tk.Tk()
        latauspalkki_tausta.title("Ladataan tiedostoja")
        latauspalkki_tausta.geometry("300x50")
        latauspalkki_tausta.attributes("-topmost", True)
        latauspalkki = ttk.Progressbar(latauspalkki_tausta, orient="horizontal", length=300)
        latauspalkki.grid(row=0, column=0, sticky="ew")

        return latauspalkki, latauspalkki_tausta

    def vaihda_aste(self):
        """ Pyydetään käyttäjältä uusi aste """
        aste = self.hae_aste()
        uusi_aste = simpledialog.askinteger(title="Aste", prompt=f"Nykyinen aste on {aste}")
        if isinstance(uusi_aste, int):
            self.ohjelma.vaihda_aste(uusi_aste)
        self.paivita_aste(self.hae_aste())

    def hae_aste(self):
        """ Noudetaan nykyinen aste ohjelmasta """
        return self.ohjelma.hae_aste()

    def paivita_aste(self, aste):
        """ Päivitetään GUI:n näyttämä aste """
        self.teksti_aste.config(text=f"aste: {aste}")
        self.paivita_solmut()

    def muodosta_lause(self):
        """
        Lähetetään ohjelmalle tekstilaatikon sisältö ja tulostetaan
        samaan laatikkoon saatu lause. Aikaisempi teksti säilyy.
        """
        alku = self.tekstilaatikko.get("1.0", tk.END).rstrip()
        lause = self.ohjelma.lauseen_muodostuksen_aloitus(alku, 100)
        if lause:
            self.tekstilaatikko.delete("1.0", tk.END)
            self.tekstilaatikko.insert("1.0", lause)
        else:
            messagebox.showerror(
                message="Teksitn muodostus ei onnistu. Oletko varmasti ladannut tiedostoja?")

    def muodosta_tarina(self):
        """
        Lähetetään ohjelmalle tekstilaatikon sisältö ja pituusrajoitus.
        Tulostetaan samaan laatikkoon saatu tarina. Aikaisempi teksti säilyy.
        """
        alku = self.tekstilaatikko.get("1.0", tk.END).rstrip()
        pituus = self.input_tarinan_pituus.get()
        try:
            pituus = int(pituus)
        except ValueError:
            pituus = 0
        pituus = min(pituus, 1000)
        self.paivita_pituus(pituus)
        tarina = self.ohjelma.tarinan_muodostuksen_aloitus(alku, pituus, 100)
        if tarina:
            self.tekstilaatikko.delete("1.0", tk.END)
            self.tekstilaatikko.insert("1.0", tarina)
        else:
            messagebox.showerror(
                message="Tekstin muodostus ei onnistu. Oletko varmasti ladannut tiedostoja?")

    def paivita_pituus(self, pituus):
        """ Päivitetään GUI:n tarinan minimipituuskenttä """
        self.input_tarinan_pituus.config(text=str(pituus))

    def paivita_solmut(self):
        """ Haetaan ohjelmasta trien solmujen lkm ja näytetään se """
        solmuja = self.ohjelma.hae_trien_koko()
        self.teksti_solmut.config(text=f"{solmuja}")

    def kopioi_teksti(self):
        """ Kopioi tekstilaatikon sisällön leikepöydälle """
        self.ikkuna.clipboard_clear()
        self.ikkuna.clipboard_append(self.tekstilaatikko.get("1.0", tk.END))

    def tyhjenna(self):
        """ Tyhjentää tekstilaatikon sisällön """
        self.tekstilaatikko.delete("1.0", tk.END)

    def tyhjenna_trie(self):
        """ Tyhentää trien """
        self.ohjelma.tyhjenna_trie()
        self.paivita_solmut()
