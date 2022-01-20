class Restoraan():
    restoraan_nimi = ""
    soogi_tyyp = ""

    def kirjelda_restoraan(self):
        kirj_tekst = self.restoraan_nimi + " pakub " + self.soogi_tyyp
        print(kirj_tekst)

    def ava_restoraan(self):
        print(self.restoraan_nimi, "on avatud!")
