#-*-coding: UTF-8 -*-

print("Olá! Você irá fazer uma viagem! Digite a distância e a velocidade média, que lhe direi o tempo de viagem")
dist = float(input("Digite a distância: "))
vel_media = float(input("Digite a velocidade média: "))

tempo = dist / vel_media

print("O tempo de viagem será: ", tempo)
