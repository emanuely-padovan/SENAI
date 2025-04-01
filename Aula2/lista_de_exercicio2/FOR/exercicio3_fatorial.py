# -*- coding: UTF-8 -*-

print("Olá, usuário! Insira um número e calcularei o seu fatorial.")
num = int(input("DIGITE UM NÚMERO: "))
fat = 1
for i in range(1,num+1):
    fat = i * fat
print("O valor do fatorial é: ", fat)
