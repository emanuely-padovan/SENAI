# -*- coding: UTF-8 -*-

print("Digite um valor e informerei quantos números estão entre 100 e 200!")

x = 0
while True:
    n = int(input("Digite aqui, ou digite 0 para sair: "))
    if n == 0:
        print("Você escolheu sair!")
        break
    elif n > 100 and n < 200:
        x+= 1
        print(x)
