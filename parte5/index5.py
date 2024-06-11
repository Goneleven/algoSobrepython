# ATIVIDADE 5
#|Elaborar um programa em Python que receba uma lista com 10 valores numéricos, gere uma nova lista onde cada elemento dessa lista é o quadrado dos elementos da primeira lista

print('programa que recebe valores numéricos e cria uma nova lista com o quadrado deles')

numeros = []
i = 0
print('digite 10 valores numéricos...')

for i in range (0,10,1):
    numero = float(input(f'insira o {i+1}° numero: '))
    numeros.append(numero)
    

quadrados = [numero ** 2 for numero in numeros]
print('lista de números digitados -', numeros)
print('lista do quadrado dos números digitados', quadrados)