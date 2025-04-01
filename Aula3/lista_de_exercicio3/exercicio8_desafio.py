# -*- coding: UTF-8 -*-

print("Olá, usuário! Digite um número e lhe direi quantos dígitos foram inseridos.")

num = int(input("Insira o número: "))
def contar_digitos(num):
    cont = 0
    while num >= 1:
        num = num/10
        cont += 1
    return cont

print(f"O seu número tem {contar_digitos(num)} digitos!")
