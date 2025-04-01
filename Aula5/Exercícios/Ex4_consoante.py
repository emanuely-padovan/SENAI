# -*- coding: UTF-8 -*-

L = []
soma = 0

for e in range(10):
    letra = str(input('Insira um caracter: '))
    L.append(letra)
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        soma += 0
    else:
        soma +=1
print(soma)
