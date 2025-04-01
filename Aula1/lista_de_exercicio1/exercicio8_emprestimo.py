#-*-coding: UTF-8 -*-

print("Olá, usuário! Informe o seu salário bruto e o valor da prestação, e lhe direi se você poderá fazer um empréstimo")
salb = float(input("Informe o seu salário bruto: "))
prestacao = float(input("Informe o valor que deseja fazer de empréstimo: "))

imped = salb - salb * prestacao / 100
if salb > imped:
    print("Você poderá realizar o seu empréstimo!")
else:
    print("Você não poderá realizar o seu empréstimo!")
