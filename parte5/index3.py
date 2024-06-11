# ATIVIDADE 3
#|Elaborar um programa em Python que receba uma lista com 9 valores numéricos, calcule e mostre a somatória dos números pares. 

vetorPar = []
vetorImpar = []
somaTotal = 0

for contador in range(0, 9):
    valor = int(input("Digite um valor Par: "))
    if(valor % 2 == 0):
        somaTotal = int(somaTotal + valor)
        vetorPar.append(valor)

    else:
        print("O número impar colocado não estara na lista")

print(f'\nOs números Pares que você colocou são:\n{vetorPar}')

print(f'A Soma total desses números é = {somaTotal}\n')
