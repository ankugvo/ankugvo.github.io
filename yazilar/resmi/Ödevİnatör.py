print("Ödevİnatör™, tüm ödevlerinizi olabildiğince geniş bir zaman aralığına sokar\n")
ilkSayfa = int(input("Ödevin ilk sayfası: "))
sonSayfa = int(input("Ödevin son sayfası: "))
sonGun = int(input("Ödev kaç gün sonraya: "))
tamSayfa = sonSayfa - ilkSayfa + 1
kalanGun = sonGun
i = 0
kalanSayfa = tamSayfa
while kalanGun > 0:
    paySayfa = kalanSayfa / kalanGun
    if paySayfa % 1 != 0:
        paySayfa -= paySayfa % 1
        paySayfa += 1
    i += 1
    if int(sonSayfa - kalanSayfa + 1) == int(sonSayfa - kalanSayfa + paySayfa):
        print(f"Gün #{i}: {int(sonSayfa - kalanSayfa + 1)}")
    else:
        print(f"Gün #{i}: {int(sonSayfa - kalanSayfa + 1)} - {int(sonSayfa - kalanSayfa + paySayfa)}")
    kalanSayfa -= paySayfa
    kalanGun -= 1
input()