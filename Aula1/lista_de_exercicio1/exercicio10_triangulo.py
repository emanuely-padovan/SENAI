#-*-coding: UTF-8 -*-

print("Olá, usuário! Informe três valores e lhe direi se eles podem formar ou não os lados de um triângulo, e qual tipo de triângulo eles podem formar")
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

if num1 == num2 and num1 != num3:
    print("É possível formar um triângulo isóceles!")
elif num1 == num2 and num1 == num3:
    print("É possível formar um triângulo equilátero!")
elif num1 != num2 and num1 != num3:
    print("É possível formar um triângulo escaleno")
else:
    num1 > num2 + num3 or num2 > num1 + num3 or num3 > num1 + num2
    print("Não é possível fazer um triângulo!")
