# -*- coding: UTF-8 -*-

print("Diga-me o valor de seu salário, e lhe direi o valor de aumento que receberá")
salario = float(input("Digite o valor de seu salário: "))

if salario > 1250.00:
    print("Você receberá 10% de aumento")
    nvalor = salario * 10 / 100
    print("Será aumentado: ", nvalor)
else:
    salario <= 1250.00
    print("Você receberá 15% de aumento")
    no_valor = salario * 15 / 100
    print("Será aumentado: ", no_valor)


