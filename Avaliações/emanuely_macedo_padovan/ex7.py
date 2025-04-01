# -*- coding: UTF-8 -*-

def potencia():
    base = int(input('Insira o número para a base: '))
    expoente = int(input('Insira um número para ficar como expoente: '))
    conta = base ** expoente
    return conta

print(f'O resultado é: {potencia()}')
