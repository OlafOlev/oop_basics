class Kasutajad():

    def __init__(self, eesnimi, perenimi):
        self.eesnimi = eesnimi
        self.perenimi = perenimi

    def maara_kasutajanimi(self, kasutajanimi):
        self.kasutajanimi = kasutajanimi
    def maara_parool(self, parool):
        self.parool = parool

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1}, kasutajanimi on {2}, parool on  {3}".format(self.eesnimi, self.perenimi, self.kasutajanimi, self.parool))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}".format(self.eesnimi))