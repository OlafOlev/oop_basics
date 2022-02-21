from praks2.kool.oppimine import *
# Loome objekti teemad kasutades "Andmed" klassi
teemad = Andmed("klass", "objekt", "parilus", "polumorfism", "kapseldus")
# Loome objekti "anna" kasutades "Opetaja" klassi
anna = Opetaja()
# Loome objekti "kadi" kasutades "Opilane" klassi
kadi = Opilane()
# Loome objekti "mati" kasutades "Opilane" klassi
mati = Opilane()
# Kutsume esile anna "opetab" meetodi
anna.opetab(teemad[4], kadi, mati)
# Kutsume esile anna "opetab" meetodi
anna.opetab(teemad[2], kadi)
# Kutsume esile mati "ise_opib" meetodi
mati.ise_opib(teemad[3])
# Prindime valja opilaste teadmised
print("Mati oskab jargmisi teemasi: " ,mati.teadmised)
print("Kadi oskab jargmisi teemasi: " ,kadi.teadmised)
# Kutsume esile opilaste "unustamine" meetodi
mati.unustamine()
kadi.unustamine()
# Prindime valja opilaste teadmised peale magamist
print("Matil ules argates meenusid jagmisied teemad: ",mati.teadmised)
print("Kadil ules argates meenusid jagmisied teemad: ",kadi.teadmised)