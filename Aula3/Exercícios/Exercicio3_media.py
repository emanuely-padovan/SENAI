# -*- coding: UTF-8 -*-

A = 0
soma = 0
print("Irei fazer a média de valores para você!")
while True:
    x = int(input("Informe os valores a serem somados para a média. Ou digite -1 para sair: "))
    if x >= 0:
        A +=1
        soma+=x
    else:
        break
    media = soma/A
print("O valor da media dos números é: ", media)
