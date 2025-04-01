#-*-coding: UTF-8 -*-
import math

print("Olá, usuário! Digite 1 número e lhe direi a raiz dele. Caso ele seja positivo ou igual a zero.")
num = int(input("Digite o valor: "))

if num >= 0:
    raiz = math.sqrt(num)
    print("O resultado é: %.2f" %raiz)
else:
    potencia = num ** 2
    print("O resultado é: ", potencia)
