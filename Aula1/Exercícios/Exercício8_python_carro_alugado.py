#-*-coding: UTF-8 -*-

print("Olá!Vamos calcula os gastos de seu carro alugado")
dias = int(input("Digite a quantidade de dias que você usou o carro alugado: "))
km = float(input("Diga quantos quilometros foram rodados nesse período: "))

preco = 60 * dias + 0.15 * km

print("O preço que você terá que pagar será: ", preco)
