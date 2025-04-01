# -*- coding: UTF-8 -*-

print('Olá, usuário! Informe o comprimento dos lados de um triângulo e direi se ele é equilátero.')

num1 = int(input('Insira o comprimento: '))
num2 = int(input('Insira o comprimento: '))
num3 = int(input('Insira o comprimento: '))

if num1 == num2 and num1 == num3:
    print('O comprimento de todos os lados do triângulo são iguais, então ele é equilátero.')
else:
    print('O triângulo não é equilátero!')
