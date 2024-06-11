# ATIVIDADE 6
#|Faça um programa em Python que leia 15 números inteiros. Determine e mostre quantas vezes o número 0 é repetido na lista. 


print('programa que recebe números 15 números inteiros e mostra quantas vezes o zero é repetido')

numeros = []
i = 0
print('digite 15 valores numéricos inteiros...')

for i in range (0,10,1):
    numero = float(input(f'insira o {i+1}° numero: '))
    numeros.append(numero)
    

contador = numeros.count(0)
print(f'o número 0 apareceu {contador} vezes')