# Escreva um programa que calcule a conta de luz de um usuário. O usuário deve entrar a quantidade de kWh.
# O cálculo da conta será o seguinte:
# Até 100 kWh - sem custo
# Os próximos 100 kWh - R$ 0,5 por kWh
# do que 200 kWh - R$ 0.8 por kWh
# Por exemplo, se o usuário consumiu 350 kWh, o cálculo será:
# 50 + (350 - 200) * 0,8 = R$ 170
# Se ele consumiu 150 kWh:
# (150 - 100) * 0,5 = R$ 25

kWh = float(input("Digite a quantidade de kWh: "))

if kWh <= 100:
    print("Sem Custo.")

else:
    if kWh <= 200:
        print("O custo é de: ", (kWh - 100) * 0.5)
    else:
        print("O custo é de: ", (50 + (kWh - 200) * 0.8))
