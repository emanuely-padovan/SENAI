# -*- coding: UTF-8 -*-

cont = 0

print("Informe o seu sexo (F ou M) e direi a quantidade de pessoas do sexo masculino! Para sair insira 0")

quant = int(input("Digite quantas pessoas: "))

for i in range (quant):
    sexo = input("Qual o sexo?: ")
    if sexo == "M" or sexo == "m":
        cont+= 1
        print(cont)
