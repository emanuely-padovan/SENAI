# -*- coding: UTF-8 -*-

print("Olá, usuário! Digite um número e contarei ele como uma contagem regressiva para o Ano Novo!!")
def contagem(x):
    for i in range(x,0,-1):
        print(i)
    print("Feliz Ano Novo!!")
x = int(input("Insira um número: "))
contagem(x)
