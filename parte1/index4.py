# ATIVIDADE 4
#|Criar um algoritmo que dados dois lados de um triângulo retângulo calcule e exiba a respectiva hipotenusa

import math

print('\n Programa que calcula a hipotenusa de um triangulo \n')

catetoOposto = float(input('Entre com o cateto OPOSTO \n'))

catetoAdjacente = float(input('Entre com o cateto ADJACENTE \n'))

hipotenusa = math.sqrt(pow(catetoOposto,2) + catetoAdjacente**2)
#sqrt é da biblioteca math e pow não, por isso não chama o método

print('Hipotenusa: {:.2f}'.format(hipotenusa))