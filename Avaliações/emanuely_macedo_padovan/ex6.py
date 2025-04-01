# -*- coding: UTF-8 -*-

print('Olá, usuário! Insira um número e direi todos os múltiplos de 5, de 0 até esse número.')

num = int(input('Insira um valor: '))

for i in range(0,num + 1):
    if i %5 == 0:
        print(i)
