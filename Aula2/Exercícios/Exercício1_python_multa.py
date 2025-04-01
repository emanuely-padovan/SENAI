# -*- coding: UTF-8 -*-

print("Olá! Vou dizer o valor da sua multa")
veloc = int(input("Qual a sua velocidade: "))

if veloc > 80:
    print("Você foi multado!")
    val_pag = (veloc - 80) * 5
    print("O valor que deverá ser pago será igual à: ", val_pag)
else:
    print("Você não foi multado!")
