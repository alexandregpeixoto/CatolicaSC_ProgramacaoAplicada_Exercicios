# Escreva um programa que receba um número do usuário e imprima seu fatorial (usando loops, e não recursão)
def calculoFatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

try:
    num = int(input("Digite um número para calcular o fatorial: "))
    if num < 0:
        print("O fatorial não está definido para números negativos.")
    else:
        resultado = calculoFatorial(num)
        print(f"O fatorial de {num} é {resultado}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")