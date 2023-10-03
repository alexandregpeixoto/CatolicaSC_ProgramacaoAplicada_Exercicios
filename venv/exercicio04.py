# Escreva um programa que receba um número de 1 a 7 e mostre o nome do dia, de forma que 1 seja domingo, 2 segunda-feira e assim por diante.

from enum import Enum

class diasDaSemana(Enum):
    Domingo = 1
    Segunda = 2
    Terca = 3
    Quarta = 4
    Quinta = 5
    Sexta = 6
    Sabado = 7

numero = 0

while(numero < 1 or numero >7):
    numero = int(input("Digite o número referente ao dia da semana: "))

dia = diasDaSemana(numero)
print(f"O dia da semana referente ao número {numero} é {dia.name}.")