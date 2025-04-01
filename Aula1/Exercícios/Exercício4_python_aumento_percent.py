#-*-coding: UTF-8 -*-

print("Digite o valor do seu salário e o percental que deseja para um aumento")
salario = float(input("Digite o valor do seu salário: "))
percentual = float(input("Digite o percentual que deseja: "))

porcent = salario * percentual / 100
nsalario = salario + porcent

print("O seu novo salário será: ", nsalario)
print("O aumento foi de: ", porcent)
