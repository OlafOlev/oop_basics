from random import randint
class Ristkulik:
    def __init__(self, laius, korgus, symbol):
        self.laius = int(laius)
        self.korgus = int(korgus)
        self.symbol = str(symbol)
    def __str__(self):
        ruut = []
        for i in range(self.korgus):
            ruut.append(self.symbol * self.laius)
        ruut = '\n'.join(ruut)
        return ruut
    def __add__(self, other):
        laius1 = self.laius.__add__(self.laius)
        korgus1 = self.korgus.__add__(self.korgus)
        ran = randint(1,2)
        if ran == 1:
            symbol1 = kujund1.symbol
        else:
            symbol1 = kujund2.symbol
        kujund3 = Ristkulik(laius1, korgus1, symbol1)
        return kujund3
kujund1 = Ristkulik(10,3,'*')
print(kujund1)
kujund2 = Ristkulik(8,3,'z')
print(kujund2)
print(kujund1 + kujund2)
