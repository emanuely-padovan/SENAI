#-*-coding: UTF-8 -*-

print("Olá, usuário! Digite dois números e irei soma-los. Depois, irei adcionar 8 ao valor caso a soma fique maior que 20 e subtrairei 5, caso o valor seja menor que 20")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
if soma > 20:
    final1 = soma + 8
    print("O valor da soma é: ", soma)
    print("O valor final é: ", final1)
else:
    soma <= 20
    final2 = soma - 5
    print("O valor da soma é: ", soma)
    print("O valor final é: ", final2)
