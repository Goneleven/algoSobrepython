#ATIVIDADE 1
#|Faça um algoritmo e fluxograma para calcular a conta final de um hóspede de um hotel fictício, contendo: o nome do hóspede, o tipo do apartamento, o número de diárias utilizadas,
#|o valor unitário da diária, o valor total das diárias, o valor do consumo interno, o subtotal, o valor da taxa de serviço e o total geral.

import math

print('\n Programa que calcula a conta final de um hóspede \n')

nomeHospede = input('Coloque seu nome: ')

tipoDeApartamento = input('\nDigite o tipo de Apartamento:\n(A) | Valor da Diária: R$150,00 \n(B) | Valor da Diária: R$100,00 \n(C) | Valor da Diária: R$75,00 \n(D) | Valor da Diária: R$50,00 \n')

numeroDiarias = int(input('Digite o número de diárias utilizadas: '))

consumoInterno = float(input('Digite o valor do Consumo Interno: R$'))


#IF/ELSE para determinar o tipoDeApartamento e Calcular a Diária:

if(tipoDeApartamento == 'A' or tipoDeApartamento == 'a'): #APARTAMENTO (A)
    valorDaDiaria = (numeroDiarias * 150.00)
    
else:
    if(tipoDeApartamento == 'B' or tipoDeApartamento == 'b'): #APARTAMENTO (B)
        valorDaDiaria = (numeroDiarias * 100.00)

    else:
        if(tipoDeApartamento == 'C' or tipoDeApartamento == 'c'): #APARTAMENTO (C)
            valorDaDiaria = (numeroDiarias * 75.00)
            
        else:
            if(tipoDeApartamento == 'D' or tipoDeApartamento == 'd'): #APARTAMENTO (D)
                valorDaDiaria = (numeroDiarias * 50.00)
                
            else: #APARTAMENTO (NÃO EXISTENTE)
                print('\n O Apartamento "', tipoDeApartamento, '" não existe, tente colocar (A), (B), (C) Ou (D)\n')
                quit()

# _______________________________________________________

# Nome & Valor da Diária & Tipo Apartamento:
print('\nOlá', nomeHospede, 'Aqui está a conta:')
print('| Tipo de Apartamento:', tipoDeApartamento)
print('| Valor total da Diária: R$', valorDaDiaria)

 # Calcular SubTotal:
subtotal = (valorDaDiaria + consumoInterno)
print('| SubTotal: R$', subtotal)

# Calcular o Valor da Taxa de Serviço:
valorTaxaServico = (0.10 * subtotal)
print('| Valor de Taxa de Serviço: R$', valorTaxaServico)

# Calcular o Total Geral:
totalGeral = (subtotal + valorTaxaServico)
print('| Valor Total Geral: R$', totalGeral, '\n')