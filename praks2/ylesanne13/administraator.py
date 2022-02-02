from praks2.ylesanne13.admin import Admin

kasutaja1 = Admin("Janre", "Liiv")
kasutaja1.maara_kasutajanimi("Janre.Liiv")
kasutaja1.maara_parool("1111")
kasutaja1.kirjelda_kasutaja()
kasutaja1.tervita_kasutaja()
valik = input("Kas soovite lisada õiguseid? jah/ei :").lower()
while valik == "jah":
    valik2 = int(input("Millist privileegi soovide lisada? 1-lubatud lisada kasutajad, 2-lubatud eemaldada kasutajad, 3 -lubatud blokeerida kasutajad, 4-muu : "))
    if valik2 == 1:
        kasutaja1.privileegid.append("lubatud lisada kasutajad")
    if valik2 == 2:
        kasutaja1.privileegid.append("lubatud eemaldada kasutajad")
    if valik2 == 3:
        kasutaja1.privileegid.append("lubatud blokeerida kasutajad")
    if valik2 == 4:
        kasutaja1.privileegid.append(input("Sisestage õigus mida tahate lisada : "))
    valik = input("Kas soovite lisada veel õiguseid? jah/ei :")
print("Kasutaja õigused on järgmised : ")
kasutaja1.naita_privileegid()
