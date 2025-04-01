#-*-coding: UTF-8 -*-

print("Olá, usuário! Informe as suas duas notas desse bimestre, e lhe direi se você será aprovado, reprovado ou ficará de recuperação!")
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

print("Sua média é igual à: ", media)

if media >= 7.0:
    print("Você foi aprovado!")
elif media < 3.0:
    print("Você foi reprovado!")
else:
    media > 3.0 and media < 7.0
    print("Você ficou de recuperação!")
