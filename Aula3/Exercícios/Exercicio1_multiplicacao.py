# -*- coding: UTF-8 -*-

print("Olá, usuário! Informe um valor e o multiplicarei por 3.")
while True:
    A = int(input("Digite o número a multiplicar por 3 ou -999 para sair: "))
    if A == -999:
        print("Você escolheu sair!")
        break
    A = A * 3
    print("O valor final é: ", A)
