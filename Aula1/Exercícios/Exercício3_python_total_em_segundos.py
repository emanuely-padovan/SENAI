#-*-coding: UTF-8 -*-

print("Digite a quantidade de dias, horas, minutos e segundos")
quant1 = int(input ("Digite o valor de dias: "))
quant2 = int(input ("Digite o valor de horas: "))
quant3 = int(input ("Digite o valor de minutos: "))
quant4 = int(input ("Digite o valor de segundos: "))

convert1_dias = ((quant1 * 24) * 60) * 60
convert2_horas = (quant2 * 60) * 60
convert3_minutos = (quant3 *60)

total = convert1_dias + convert2_horas + convert3_minutos + quant4

print("O resultado da média é: ", total)
