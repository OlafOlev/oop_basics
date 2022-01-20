from praks2.ylesanne8.tootajad import Inimene
toodaja1 = Inimene("Janre", "Liiv", 10)
toodaja2 = Inimene("Viktor", "Lumiste", 9)
toodaja3 = Inimene("Gervin", "Luide", 8)
toodaja1.tutvustus()
toodaja2.tutvustus()
toodaja3.tutvustus()
if toodaja1.kutsekvalifikatsioon > toodaja2.kutsekvalifikatsioon:
    if toodaja2.kutsekvalifikatsioon > toodaja3.kutsekvalifikatsioon:
        print("Toodaja " + toodaja3.eesnimi, toodaja3.perenimi + " olete vallandatud!")
        del(toodaja3)
    else:
        print("Toodaja " + toodaja2.eesnimi + toodaja2.perenimi + "olete vallandatud!")
        del(toodaja2)
elif toodaja1.kutsekvalifikatsioon < toodaja3.kutsekvalifikatsioon:
    print("Toodaja " + toodaja1.eesnimi + toodaja1.perenimi + "olete vallandatud!")
    del(toodaja1)
input()