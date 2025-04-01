# -*- coding: UTF-8 -*-

L = []
acum = 0

for lista in range(4):
    num = int(input('Insira sua nota: '))
    L.append(num)
    acum = acum + num

media = acum/4
print(media)
