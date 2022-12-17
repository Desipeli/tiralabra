import requests
import random
from bs4 import BeautifulSoup as BS


class GutenbergLukija:
    def __init__(self, url: str = None) -> None:
        """ 
        url: sivu, jossa kirjat on listattu
        self._book_urls: Lista kirjojen linkeistä
        """
        self._base_url = "https://www.gutenberg.org"
        self._url = url
        self._kirjalista = []
        self.hae_linkit()

    def aseta_url(self, url: str):
        """ Url jossa kirjat listattu """
        self._url = url

    def sekoita_kirjalista(self):
        """ Sekoitetaan kirjalista """
        random.shuffle(self._kirjalista)

    def kirjalistan_koko(self):
        return len(self._kirjalista)

    def hae_kirja(self):
        """ Haetaan listan viimeinen kirja """
        if len(self._kirjalista) == 0:
            return False
        linkki = self._kirjalista.pop()
        teksti = self.hae_teksti(linkki)
        print(linkki)
        return teksti

    def hae_linkit(self):
        """ 
        Etsitään kaikki kirjalinkit sivulta
        """
        if not self._url or not self._base_url:
            return False

        self._kirjalista = []

        req = requests.get(self._url)
        keitto = BS(req.text, "html.parser")

        for linkki in keitto.find_all("a"):
            link_teksti = linkki.get("href")
            if link_teksti and "ebooks" in link_teksti:
                self._kirjalista.append(link_teksti)

    def hae_teksti(self, link: str):
        """ Haetaan sivulla oleva teksti """
        kokolinkki = self._base_url + link + ".txt.utf-8"
        req = requests.get(kokolinkki)
        return req.content.decode("utf-8")
            



if __name__ == "__main__":
    gr = GutenbergLukija("https://www.gutenberg.org/browse/languages/fi")
    gr.hae_linkit()
    gr.sekoita_kirjalista()
    kirja = gr.hae_kirja()
    print(kirja)