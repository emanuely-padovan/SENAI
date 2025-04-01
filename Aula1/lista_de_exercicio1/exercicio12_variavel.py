#-*-coding: UTF-8 -*-

print("Olá, usuário! Me diga dois números e os organizarei em ordem crescente")
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 > num2:
    new1 = num1
    new2 = num2
    print("A ordem é: ",(new2),(new1))
else:
    new1 = num1
    new2 = num2
    print("A ordem é: ",(new1), (new2))
