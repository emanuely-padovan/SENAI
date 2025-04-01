#-*-coding: UTF-8 -*-

print("Olá, usuário! Informe a sua idade e direi a sua classificação etária")
idade = int(input("Indique a sua idade: "))

if idade < 2:
    print("Você é: BEBÊ")
elif idade > 2 and idade < 12:
    print("Você é: CRIANÇA")
elif idade > 12 and idade < 23:
    print("Você é: ADOLESCENTE")
elif idade > 23 and idade < 70:
    print("Você é: ADULTO")
else:
    idade > 70
    print("Você é: IDOSO")
