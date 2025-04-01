# -*- coding: UTF-8 -*-

print("Olá, usuário! Irei calcular o volume de um cilindro.")
def volume():
    altura = float(input("Insira a altura do cilindro: "))
    raio = float(input("Insira o raio do cilindro: "))
    volumec = 3.14 * (raio ** 2) * altura
    return volumec

print("O volume do cilindro é: ", volume())
