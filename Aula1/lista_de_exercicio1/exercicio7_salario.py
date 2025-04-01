#-*-coding: UTF-8 -*-

print("Olá, usuário! Irei lhe dizer o valor de seu salário líquido")
hora = float(input("Informe quantas horas você trabalhou: "))

sal = 19.50 * hora

print("O seu salário foi de: ", sal)

if sal > 1500:
    nsal = sal - sal * 10 / 100 
    print("O seu salário é igual à: ", nsal)
