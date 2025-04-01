# -*- coding: UTF-8 -*-

print("Olá, usuário! Digite um número e farei a tabuada desse número.")
def tabela(num):
    for c in range (1,11):
            print(num,"x",c,"=", (num*c))
num = int(input("Insira um valor: "))
tabela(num)
