# -*- coding: UTF-8 -*-

acum = 0

for aluno in range(10):
    num = str(input('Insira os  nomes dos alunos: '))
    L = []
    for lista1 in range(4):
        num = float(input('Insira uma nota: '))
        L.append(num)
        soma = num + num + num + num
    media = soma /4
    print(media)
