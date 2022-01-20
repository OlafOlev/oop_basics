class Restoraan():
    teenindatud_kylastajad = 0
    def __init__(self, restoraan_nimi, soogi_tyyp):
        self.restoraan_nimi = restoraan_nimi
        self.soogi_tyyp = soogi_tyyp
    def kirjelda_restoraan(self):
        kirj_tekst = self.restoraan_nimi + " pakub " + self.soogi_tyyp
        print(kirj_tekst)

    def ava_restoraan(self):
        print(self.restoraan_nimi, "on avatud!")
    def maara_teenindatud_kylalised(self,teenindatud_kylalised):
        self.teenindatud_kylastajad = teenindatud_kylalised
    def suurenda_teenindatud_kylalised(self, suurentatud_teenindatud_kylalised):
        self.teenindatud_kylastajad +=  suurentatud_teenindatud_kylalised

