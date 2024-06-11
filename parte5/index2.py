# ATIVIDADE 2
#|Elabore um programa em Python que receba uma lista de 8 números inteiros e imprima os elementos pares do vetor. 

vetorPar = []
vetorImpar = []

for contador in range(0, 8):
    valor = int(input("Digite um valor: "))
    if(valor % 2 == 0):
        vetorPar.append(valor)

    else:
        vetorImpar.append(valor)

print(f'Os números Pares que você colocou são:\n{vetorPar}')

print(f'Os números Impares que você colocou são:\n{vetorImpar}')