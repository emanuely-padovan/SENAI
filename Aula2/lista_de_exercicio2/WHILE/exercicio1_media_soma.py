# -*- coding: UTF-8 -*-

soma = 0
contador = 0

print("Olá, usuário! Informe valores e calcularei a soma e a média deles.")
while True:
    num = float(input("Insira um valor, ou digite um número negativo para sair: "))
    if num < 0:
        break
    soma += num
    contador += 1
    media = soma / contador
print("A soma dos valores é: ", soma)
print("A média dos valores é: ", media)
