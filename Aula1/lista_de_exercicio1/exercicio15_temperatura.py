#-*-coding: UTF-8 -*-

print("Olá, usuário! Informe a temperatura atual, e direi se está: MUITO FRIO, FRIO, AGRADÁVEL, CALOR ou MUITO QUENTE")
temp = int(input("Informe a temperatura atual: "))

if temp <= 15:
    print("O clima está: Muito Frio!")
elif temp >= 15 and temp < 23:
    print("O clima está: Frio!")
elif temp >= 23 and temp < 26:
    print("O clima está: Agradável!")
elif temp >= 26 and temp < 30:
    print("O clima está: Calor!")
else:
    temp > 31
    print("O clima está: Muito quente!")
