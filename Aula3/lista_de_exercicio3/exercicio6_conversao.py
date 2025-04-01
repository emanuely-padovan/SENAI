# -*- coding: UTF-8 -*-

print("Olá! Coloque a temperatura, depois insira um tipo de conversão (Celsius para Fahrenheit e vice-versa).")

def conversao():
    temperatura = float(input("Insira a temperatura: "))
    convert = input("Insira o tipo de conversão: ")

    if convert == 'Celsius para Fahrenheit' or 'celsius para fahrenheit':
        conta1 = temperatura * 9/5 + 32
        print("Você escolheu converter celsius para fahrenheit!")
        print("O resultado é: ", conta1)
    elif convert == 'Fahrenheit para Celsius' or 'fahrenheit para celsius':
        conta2 = temperatura * 1,8 + 32
        print("Você escolheu converter fahrenheit para celsius!")
        print("O resultado é: ", conta2)
        
conversao()
