# Escreva um programa que imprima os 10 primeiros números pares.

def imprimeNumerosPares():
    count = 0
    numero = 2

    while count < 10:
        print(numero)
        numero += 2
        count += 1

# Chama a função para imprimir os números pares
imprimeNumerosPares()