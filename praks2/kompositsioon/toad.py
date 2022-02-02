from praks2.kompositsioon.tuba import Tuba
tuba = Tuba(float(input("Sisestage toa pikkus:")), float(input("Sisestage toa laius:")), float(input("Sisestage toa korgus:")))
tuba.lisa_Aknad_uks(float(input("Sisestage ukse laius:")), float(input("Sisestage ukse kõrgus:")))
valik = input("Kas toas on aknaid? jah/ei : ").lower()
while valik == "jah":
    tuba.lisa_Aknad_uks(float(input("Sisestage akna laius:")), float(input("Sisestage akna korgus:")))
    valik = input("Kas toas on veel aknaid? jah/ei : ").lower()
tuba.tapeedi_rull(float(input("Sisestage tapeedi rulli laius: ")), float(input("Sisestage tapeedi rulli pikkus: ")))
print("Tapeeti on vaja {0} m2, mis on {1} rulli".format(tuba.toopindala(), round(tuba.tapeedi_rulle)))