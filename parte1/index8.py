# ATIVIDADE 8
#|Faça um algoritmo que receba o custo de um espetáculo teatral e o preço do convite deste espetáculo.
#|Esse algoritmo deve calcular e mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.

print('\n Programa que calcula a quantidade de Convites a serem vendidos \n')

custoDoEspetaculo = float(input('Digite o custo necessário para o espetáculo teatral: '))

valorDoConvite = float(input('Digite o valor do convite: '))

vendasNecessarias = (custoDoEspetaculo / valorDoConvite)

print('\nSerá necessário vender: {:.0f}'.format(vendasNecessarias), 'Ingressos!')