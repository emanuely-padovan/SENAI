# -*- coding: UTF-8 -*-

soma = 0
soma1 = 0

print("Olá, usuário! Insira um valor inteiro e positivo. No final lhe direi a soma dos números ímpares e a soma dos números pares.")

while True:
    num = int(input("Insira um valor, ou digite um número maior que 1000 para sair: "))
    if num >= 1000:
        print("Você escolheu sair!")
        break
    elif num %2 == 0:
        soma += num
    elif num %2 != 0:
        soma1 += num
print("A soma dos números pares é: ", soma)
print("A soma dos números ímpares é: ", soma1)
