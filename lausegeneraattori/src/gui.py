import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from ohjelma import Ohjelma
from tiedostonlukija import TiedostonLukija

class GUI:
    """ Graafinen käyttöliittymä """
    def __init__(self, ohjelma: "Ohjelma", tiedostonlukija: "TiedostonLukija") -> None:
        """ Konstruktori

        """
        self.ohjelma = ohjelma
        self.tiedostonlukija = tiedostonlukija

        self.ikkuna = tk.Tk()
        self.ikkuna.rowconfigure(0, minsize=400, weight=1)
        self.ikkuna.columnconfigure(1, minsize=300, weight=1)
        self.ikkuna.title("Lausegeneraattori")

        self.tekstilaatikko = tk.Text(self.ikkuna)
        self.toimintokehys = tk.Frame(self.ikkuna, relief=tk.RAISED, bd=2)
        nappi_lataa = tk.Button(self.toimintokehys,
            text="Lataa tiedostoja",
            command=self.lataa_tiedostoja)
        nappi_aste = tk.Button(self.toimintokehys, text="Vaihda aste", command=self.vaihda_aste)
        self.teksti_aste = tk.Label(self.toimintokehys, text=f"aste: ")
        self.teksti_solmut = tk.Label(self.toimintokehys, text="Triessä solmuja: 0")
        nappi_lause = tk.Button(self.toimintokehys, text="Muodosta Lause", command=self.muodosta_lause)
        tarinan_pituus = tk.Label(self.toimintokehys, text="tarinan pituus min")
        self.input_tarinan_pituus = tk.Entry(self.toimintokehys, text="20")
        nappi_tarina = tk.Button(self.toimintokehys, text="Muodosta tarina", command=self.muodosta_tarina)
        nappi_kopioi = tk.Button(self.toimintokehys, text="Kopioi", command=self.kopioi_teksti)

        nappi_lataa.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.teksti_aste.grid(row=1, column=0, sticky="ew", padx=5)
        self.teksti_solmut.grid(row=2, column=0, sticky="ew", padx=5)
        nappi_aste.grid(row=3, column=0, sticky="ew", padx=5)
        nappi_lause.grid(row=4, column=0, sticky="ew", padx=5)
        tarinan_pituus.grid(row=5, column=0, sticky="ew", padx=5)
        self.input_tarinan_pituus.grid(row=6, column=0, sticky="ew", padx=5)
        nappi_tarina.grid(row=7, column=0, sticky="ew", padx=5)
        nappi_kopioi.grid(row=8, column=0, sticky="ew", padx=5)

        self.toimintokehys.grid(row=0, column=0, sticky="ns")
        self.tekstilaatikko.grid(row=0, column=1, sticky="nsew")

        self.paivita_aste(self.hae_aste())
        self.ikkuna.mainloop()

    def lataa_tiedostoja(self):
        """ Voidaan ladata monta tiedostoa kerralla """
        tiedostojen_nimet = filedialog.askopenfilenames(
            initialdir= os.path.join(os.path.dirname(__file__), "data"),
            title="valitse tiedosto(t)",
            filetypes= (("Text files",
                        "*.txt*"),
                        ("all files",
                        "*.*")))
        for nimi in tiedostojen_nimet:
            sisalto = self.tiedostonlukija.lue(nimi)
            onnistui = self.ohjelma.lataa_tiedoston_sisalto(sisalto)
            if onnistui:
                print(nimi)
            else:
                print("Virhe: ", nimi)
        self.paivita_solmut()

    def vaihda_aste(self):
        """ Pyydetään käyttäjältä uusi aste """
        aste = self.hae_aste()
        uusi_aste = simpledialog.askinteger(title="Aste", prompt=f"Nykyinen aste on {aste}")
        self.ohjelma.vaihda_aste(uusi_aste)
        self.paivita_aste(self.hae_aste())

    def hae_aste(self):
        """ Noudetaan nykyinen aste ohjelmasta """
        return self.ohjelma.hae_aste()

    def paivita_aste(self, aste):
        """ Päivitetään GUI:n näyttämä aste """
        self.teksti_aste.config(text=f"aste: {aste}")

    def muodosta_lause(self):
        alku = self.tekstilaatikko.get("1.0", tk.END)
        lause = self.ohjelma.lauseen_muodostuksen_aloitus(alku)
        print(lause)
        if lause:
            self.tekstilaatikko.delete("1.0", tk.END)
            self.tekstilaatikko.insert("1.0", lause)
        else:
            messagebox.showerror(
                message="Teksitn muodostus ei onnistu. Oletko varmasti ladannut tiedostoja?")

    def muodosta_tarina(self):
        alku = self.tekstilaatikko.get("1.0", tk.END)
        pituus = self.input_tarinan_pituus.get()
        try:
            pituus = int(pituus)
        except ValueError:
            pituus = 0
        if pituus > 1000: pituus = 1000
        self.paivita_pituus(pituus)

        tarina = self.ohjelma.tarinan_muodostuksen_aloitus(alku, pituus)
        print(tarina)
        if tarina:
            self.tekstilaatikko.delete("1.0", tk.END)
            self.tekstilaatikko.insert("1.0", tarina)
        else:
            messagebox.showerror(
                message="Tekstin muodostus ei onnistu. Oletko varmasti ladannut tiedostoja?")

    def paivita_pituus(self, pituus):
        """ Päivitetään GUI:n tarinan minimipituuskenttä """
        self.input_tarinan_pituus.config(text=pituus)

    def paivita_solmut(self):
        """ Haetaan ohjelmasta trien solmujen lkm ja näytetään se """
        solmuja = self.ohjelma.hae_trien_koko()
        self.teksti_solmut.config(text=f"triessä solmuja: {solmuja}")

    def kopioi_teksti(self):
        self.ikkuna.clipboard_clear()
        self.ikkuna.clipboard_append(self.tekstilaatikko.get("1.0", tk.END))
