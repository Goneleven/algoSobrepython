# ATIVIDADE 8 
#|Elabore um algoritmo e respectivo programa em Python que realize o que se pede: 
#|- leia valores numéricos de entrada até receber uma informação de finalização pelo usuário; - guarde estes valores numa lista; 
#|- mostre estas informações em ordem crescente e depois decrescente; - calcule e mostre a média destes valores.

print('programa que guarda valores em uma lista e mostra em ordem crescente, decrescente e a média dos números')

numeros = []

print('\ndigite os valores numéricos (digite "sair" para terminar)\n')

while True:
    valor = input('insira um valor: ')

    if valor == "sair":
        break

    else:
        numero = float(valor)
        numeros.append(numero)


# ordem crescente e decrescente
ordenado_crescente = sorted(numeros)
ordenado_decrescente = sorted(numeros, reverse=True)
print('\nValores em ordem crescente:', ordenado_crescente)
print('Valores em ordem decrescente:', ordenado_decrescente)


# média dos números

media = sum(numeros) / len(numeros)
print('A média dos números é igual a ', media)