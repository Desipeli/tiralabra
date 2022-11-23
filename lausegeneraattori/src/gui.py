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
        nappi_lause = tk.Button(self.toimintokehys, text="Muodosta Lause", command=self.muodosta_lause)

        nappi_lataa.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.teksti_aste.grid(row=1, column=0, sticky="ew", padx=5)
        nappi_aste.grid(row=2, column=0, sticky="ew", padx=5)
        nappi_lause.grid(row=3, column=0, sticky="ew", padx=5)

        self.toimintokehys.grid(row=0, column=0, sticky="ns")
        self.tekstilaatikko.grid(row=0, column=1, sticky="nsew")

        self.paivita_aste(self.hae_aste())
        self.ikkuna.mainloop()

    def lataa_tiedostoja(self):
        """ Voidaan ladata monta tiedostoa kerralla """
        print(os.getcwd())
        tiedostojen_nimet = filedialog.askopenfilenames(
            initialdir= "/",
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
                message="Lauseenmuodostus ei onnistu. Oletko varmasti ladannut tiedostoja?")

if __name__ == "__main__":
    import jasennin, arpa
    GUI(Ohjelma(jasennin.Jasennin(), arpa.Arpa()))