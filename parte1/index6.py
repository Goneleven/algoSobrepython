# ATIVIDADE 6
#|Faça um algoritmo que receba um número positivo e maior que zero, calcule e mostre:  
#|o número digitado ao quadrado;
#|a raiz quadrada do número digitado; 

import math

print('\n Programa que calcula o Número ao quadrado e mostra a Raiz quadrada \n')

numeroA = int(input('Escreva um número maior que 0 \n'))

if(numeroA <= 0):
    print('Eu falei! Não escolha o número zero! E Nem número negativo')

else:
    numeroQuadrado = numeroA * numeroA
    print(numeroA,'² =', numeroQuadrado)

    raizQuadrada = math.sqrt(numeroA)
    print('√', numeroA, '=', raizQuadrada)
