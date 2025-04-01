#-*-coding: UTF-8 -*-

print("Digite o preço do seu produto e seu percentual de desconto, e lhe direi o quanto recebeu de desconto e o preço a pagar")
merc = float(input("Digite o valor da mercadoria: "))
descont = float(input("Digite o valor a descontar: "))


desconto = merc * descont / 100
np = merc - desconto

print("O preço da mercadoria ficou: ",np)
print("O desconto foi de: ",desconto)
