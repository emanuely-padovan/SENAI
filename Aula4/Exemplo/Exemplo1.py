# -*- coding: UTF-8 -*-

resultado = 0
def soma():
    global resultado
    num1 = int(input("Digite um valor: "))
    num2 =int(input("Digite um valor: "))
    resultado = num1 + num2

soma()
print("O resultado é: ", resultado)
