# -*- coding: UTF-8 -*-

def maior():
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite um valor: "))

    if num1 > num2:
        return num1
    else:
        return num2
print("O maior é: ", maior())
