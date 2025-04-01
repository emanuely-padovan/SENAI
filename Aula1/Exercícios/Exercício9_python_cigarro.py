#-*-coding: UTF-8 -*-

print("Olá! Vou calcular a redução do tempo de vida, fumando cigarros")
cig = int(input("Diga a quantidade de cigarros fumados: "))
anos = float(input("Diga a quantidade de anos fumados: "))

total_cig = cig * anos * 365
mino_perd = total_cig * 10
dias = mino_perd / 60 / 24

print("O tempo de vida perdido foi de: .2f ", dias)
