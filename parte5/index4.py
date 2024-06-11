# ATIVIDADE 4
#|Elaborar um programa em Python que receba uma lista com 12 números e imprima quais são os números que estão armazenados nas posições de índice ímpar. 

vetorImpar = []
vetorPar = []

for contador in range(0, 12):
    valor = int(input("Digite um valor: "))
    if(valor % 2 != 0):
        vetorImpar.append(valor)

    else:
        vetorPar.append(valor)

print(f'Os números Impares que você colocou são:\n{vetorImpar}')

print(f'Os números Pares que você colocou são:\n{vetorPar}')