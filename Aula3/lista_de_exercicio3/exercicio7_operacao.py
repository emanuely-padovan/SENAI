# -*- coding: UTF-8 -*-

print("Olá, usuário! Insira dois valores e o tipo de operação (+, -, x e /) que você deseja que seja executada. ")
def calculo():
    valor1 = float(input("Insira um valor: "))
    valor2 = float(input("Insira um valor: "))
    operador = input("Insira o operador: ")

    if operador == '+' :
        soma = valor1 + valor2
        print("Você escolheu somar os valores!")
        print("O resultado final é: ", soma)
 
    elif operador == '-' :
        subtração = valor1 - valor2
        print("Você escolheu subtrair os valores!")
        print("O resultado final é: ", subtração)

    elif operador == '*' :
        multiplicação = valor1 * valor2
        print("Você escolheu multiplicar os valores!")
        print("O resultado final é: ", multiplicação)

    elif operador == '/' :
        divisão = valor1 / valor2
        print("Você escolheu dividir os valores!")
        print("O resultado final é: ", divisão)
        
calculo()
