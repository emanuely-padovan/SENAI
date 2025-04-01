#-*-coding: UTF-8 -*-
import math

print("Olá, usuário! Informe o seu peso e a sua altura, e lhe direi se está com um peso favorável ou não!")
peso = int(input("Informe o seu peso atual: "))
altura = float(input("Informe a sua altura: "))

calculo = peso / altura ** 2

print("O seu IMC é igual à: %.2f " %calculo)

if calculo < 20:
    print("Sua situação é: Abaixo do peso!")
elif calculo >= 25:
    print("Sua situação é: Peso Normal!")
elif calculo >= 30:
    print("Sua situação é: Sobre peso!")
elif calculo >= 40:
    print("Sua situação é: Obeso!")
else:
    calculo >= 40
    print("Sua situação é: Obeso Mórbido!")
