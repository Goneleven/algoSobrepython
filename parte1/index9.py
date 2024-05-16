# ATIVIDADE 9
#|Faça um algoritmo que receba o peso de uma pessoa em quilos. Calcule e mostre:  
#|O novo peso se a pessoa engordar 15% sobre o peso digitado; 
#|O novo peso se a pessoa emagrecer 20% sobre o peso digitado; 

print('\n Programa que calcula o peso \n')


peso = float(input('digite seu peso: '))

engordar = peso * 1.15 

emagracer = peso * 0.8 

print( '\nCaso engorde 15%, seu peso será:', engordar )

print ( 'Caso emagreça 20%, seu peso será:', emagracer)