from os import system as cls
print("bismillahirrahmanirahim ")
print("allahım bildiğimi yazdır ")
print("bilmediğimi attır ")
print("attığımı tuttur ")
input("amin ")
from random import *
list = ["düşkün","erkân","ocakzade","çelebi","dede", "mürşit", "peyik", "davetçi", "rehber","gözcü","bekçi","kapıcı","zâkir","âşık","çeralcı","delilci","ferrâş","süpürgeci","İznikçi","meydancı","sofracı","kurbancı","lokmacı","sakka","İbrikçi","pervane","semahçı", "ikrar cemi","abdal musa cemi","görgü cemi","muhasiplik","İkrar","nasip alma"]
answer = ["suçlu","cem düzen","ehlibeyt soy","hbv soy","lider","lider","davetiye","davetiye","dede yardım", "rehber yardım güvenlik","ev güvenlik","ev güvenlik", "bağlama mersiye", "bağlama mersiye","çeral aydınlat","çeral aydınlat","hademe","hademe","ayakkabı","ayakkabı","yemek","yemek","yemek","su","su","semah","semah", "yol bağlılık","her şey iyi","öz sorgu","alevi nikah","bektaşi nikah","bektaşi nikah"]
true, false = 0, 0
while len(answer) != 0:
    x = randint(0, len(answer) - 1)
    y = input(f"{list[x].capitalize()} ne demek?\nCevap: ")
    if y == answer[x]:
        input("Bildiniz! ")
        true += 1
    else:
        itiraz = input(f"Bilemediniz!\nCevap: {answer[x]} ")
        if itiraz == 0:
            true += 1
        else:
            false += 1
    del list[x]
    del answer[x]
    cls("cls")
print(f"Skorunuz: {(true / (true + false)) * 100}")