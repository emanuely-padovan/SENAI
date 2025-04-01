# -*- coding: UTF-8 -*-

print("Digite um valor e informerei quantos números foram digitados!")
x = 0
while True:
    n = int(input("Digite aqui, ou digite 0 para sair: "))
    if n == 0:
        print("Você escolheu sair!")
        break
    elif n > 0:
        x+= 1
        print(x)
