# -*- coding: UTF-8 -*-

print('Olá, usuário! Insira um número e classificarei se ele é/está: Menor que 10, entre 10 e 20 ou maior que 20.')

n = int(input('Insira um número: '))

if n < 10:
    print(f'O número {n} é menor que 10!')
elif n >= 10 and n <= 20:
    print(f'O número {n} está entre 10 e 20!')
else:
    print(f'O número {n} é maior que 20!')
