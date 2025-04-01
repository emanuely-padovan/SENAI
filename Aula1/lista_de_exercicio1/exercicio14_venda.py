#-*-coding: UTF-8 -*-

print("Olá, usuário! Informe o valor do produto, e lhe direi o valor de venda de um produto")
prod = float(input("Informe o valor do produto: "))

if prod <= 20:
    prod2  = prod + prod * 45 / 100
    print("O valor do produto deverá ser: ", prod2)
else:
    prod3 = prod + prod * 30 / 100
    print("O valor do produto deverá ser: ", prod3)
