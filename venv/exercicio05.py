# Escreva um programa que peça três números ao usuário e mostre o maior deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

listaDeNumeros = []

listaDeNumeros.append(numero1)
listaDeNumeros.append(numero2)
listaDeNumeros.append(numero3)

maiorValor = max(listaDeNumeros)

print("Lista:", listaDeNumeros)
print("O maior valor é: ", maiorValor)