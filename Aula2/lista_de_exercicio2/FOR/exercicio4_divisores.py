# -*- coding: UTF-8 -*-

print("Olá, usuário! Insira um número e direi os possíveis divisores dele.")
num = int(input("Digite o número: "))

for i in range(1,num + 1):
    if num % i == 0:
        print("Os possíveis divisores são: ", i)
