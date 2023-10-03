# Escreva um programa que receba o custo de um produto e mostre o imposto a ser pago de acordo com o seguinte critério;
# > R$ 1000 - Taxa 15%
# R$ 500 < custo <= R$ 1000 - Taxa 10%
# <= R$ 500  - Taxa 5%

valorDoProduto = float(input("Digite o valor do produto: "))

if valorDoProduto > 1000:
    print("O valor do imposto será de R$", (valorDoProduto * 0.15))
elif valorDoProduto >= 500 and valorDoProduto <= 1000:
    print("O valor do imposto será de R$", (valorDoProduto * 0.10))
else:
    print("O valor do imposto será de R$", (valorDoProduto * 0.05))