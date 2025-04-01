# -*- coding: UTF-8 -*-

print("Olá, usuário! Irei lhe dizer se um número é primo ou não.")

def primo(x):
    cont = 0
    for i in range(1,x):
        if x %i == 0:
            cont+= 1
    if cont == 1:
        return f"{x} é primo!"
    else:
        return f"{x} não é primo!"
num = int(input("Digite um número: "))
print (primo(num))
