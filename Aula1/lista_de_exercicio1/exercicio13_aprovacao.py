#-*-coding: UTF-8 -*-

print("Olá, usuário! Diga três notas suas, e o seu número de faltas. Lhe direi se está: APROVADO, REPROVADO POR FALTA ou REPROVADO POR MÉDIA")
nota1 = float(input("Insira a sua primeira nota: "))
nota2 = float(input("Insira a sua segunda nota: "))
nota3 = float(input("Insira a sua terceira nota: "))
faltas = int(input("Insira o número de faltas: "))

media = (nota1 + nota2 + nota3) / 3
freq = faltas - faltas * 25 / 100

print("Sua media foi: ", media)

if media >= 7.0 and freq >= 80:
    print("Você foi aprovado!")
elif media >= 7.0 and freq < 80:
    print("Você foi reprovado por falta!")
elif media < 7.0 and freq < 80:
    print("Você foi reprovado por falta!")
else:
    media < 7.0 and freq >= 80
    print("Você foi reprovado por média!")
