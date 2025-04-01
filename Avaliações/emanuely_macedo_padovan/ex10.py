# -*- coding: UTF-8 -*-

print('Olá, usuário! Informe o valor da conta de restaurante que recebeu e calcularei a taxa de serviço.')

valor = float(input('Insira o valor da conta: '))

if valor > 200:
    taxa = valor * 8 / 100
    n_valor = valor + taxa
    print(f'O valor da taxa de serviço é: {taxa:.2f}')
    print(f'O valor a ser pago é: {n_valor}')
else:
    taxa = valor * 10 / 100
    n_valor = valor + taxa
    print(f'O valor da taxa de serviço é: {taxa:.2f}')
    print(f'O valor a ser pago é: {n_valor}')
