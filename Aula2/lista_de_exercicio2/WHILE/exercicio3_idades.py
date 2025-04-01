# -*- coding: UTF-8 -*-


soma21 = 0
soma50 = 0

print("Olá, usuário! Insira uma idade e, no final, direi o total de pessoas que têm menos que 21 e mais de 50.")

while True:
    idade = int(input("Insira sua idade, ou digite -99 para sair: "))

    if idade == -99:
        print("Você escolheu sair!")
        break

    elif idade <= 21 and idade < 50:
        soma21 +=1

    elif idade >= 50:
        soma50 +=1
print("A soma das idades com a idade menor que 21 anos é: ", soma21)
print("A soma das idades com a idade maior que 50 anos é: ", soma50)
