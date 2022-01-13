class Kasutajad():
    eesnimi = ""
    perenimi = ""
    gmail = ""
    vanus = 0

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1}, vanus on {2}, gmail on {3}".format(self.eesnimi, self.perenimi, self.vanus, self.gmail))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}".format(self.eesnimi))