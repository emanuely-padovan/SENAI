#-*-coding: UTF-8 -*-

print("Olá, usuário! Digite dois números inteiros, e lhe informerei se o primeiro é divisível pelo segundo")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo valor: "))

if a %b == 0:
    print("O primeiro número é divisível pelo segundo!")
else:
    print("O primeiro não é divisível pelo segundo!")
