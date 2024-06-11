# ATIVIDADE 1
#|Elabore um programa em Python que receba uma lista com 10 números reais e imprima os números maiores do que 15. 

print("\n Programa que lista 10 numeros e mostre os maiores que 15\n")

# Recebendo 10 números
numeros = []
for i in range(10):
    numero = int(input("Digite o {}º número: ".format(i+1)))
    numeros.append(numero)

# Mostrando os números maiores que 15
print("Números maiores que 15 são:")
for numero in numeros:
    if (numero > 15):
        print(numero)
        