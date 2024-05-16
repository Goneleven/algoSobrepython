# ATIVIDADE 5
#|Faça um algoritmo que receba o número de horas trabalhadas e o valor do salário mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo: 
#|o valor da hora trabalhada vale a metade do salário mínimo; 
#|o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada; 
#|o imposto equivale a 3% do salário bruto; 
#|o salário a receber equivale ao salário bruto menos o imposto. 

import math

print('\n Programa que recebe horas trabalhadas e Salário minimo \n')

horaTrabalhada = int(input('Digite horas trabalhadas \n'))

salario = float(input('Digite o Salário minimo atual \n'))/2

salarioBruto = (salario * horaTrabalhada)
print(salarioBruto)

imposto = (salarioBruto * 0.03)

salario = salarioBruto - imposto

print('Salario atual: \n', salario)