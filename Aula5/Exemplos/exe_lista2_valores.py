# -*- coding: UTF-8 -*-


# Criando a lista (definindo os valore com 0 apenas para ter a quantidade de intens.)
numeros = [0, 0, 0, 0, 0]

#Navegar pelo While
x = 0

while x < 5:
#Essa linha está pegando o valor para inserir na Lista
    numeros[x] = int(input("Número %d: " % (x + 1)))
#contador do While
    x += 1

while True:
    #Essa linha está pegando o valor do índice para mostrar o valor inserido
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    #Verificando saída do While True 
    if escolhido == 0:
        break
    #Mostrando valor de acordo com o índice tirando 1 para agradar o usuário
    print ("Você escolheu o número: %d" % (numeros[escolhido - 1]))
