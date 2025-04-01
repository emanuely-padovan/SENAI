# -*- coding: UTF-8 -*-

def area():
    lado1 = float(input("Digite a base do triângulo: "))
    lado2 = float(input("Digite a altura do triângulo: "))
    areo = lado1 * lado2 / 2
    return areo

print("O resultado é: ", area())
