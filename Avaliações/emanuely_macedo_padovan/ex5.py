# -*- coding: UTF-8 -*-

print('Olá, funcionário! Informe o seu salário atual e calcularei o valor de seu bônus.')

s = float(input('Insira o seu salário: '))

if s < 1500:
    bonus = s * 15 / 100
    sal = s + bonus
else:
    bonus = s * 10 / 100
    sal = s + bonus

print(f'O seu salário de {s} irá receber um bônus de {bonus:.2f}.')
print(f'O seu salario de {s} passa a ser {sal:.2f}')
