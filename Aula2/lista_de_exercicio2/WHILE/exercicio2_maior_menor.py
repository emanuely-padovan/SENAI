# -*- coding: UTF-8 -*-

print("Olá, usuário! Insira valores e no final direi qual é o MAIOR e o MENOR.")
num = float(input("Insira um valor, ou digite um número negativo para sair: "))

maior = num
menor = num
while True:
    num = float(input("Insira um valor, ou digite um número negativo para sair: "))
    if num < 0:
        print("Você escolheu sair!")
        break
    
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print("O maior número é: ", maior)
print("O menor número é: ", menor)
