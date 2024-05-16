# ATIVIDADE 1 & 2
#|Criar um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:  
#|A idade desta pessoa hoje; 
#|A idade desta pessoa em 2025. 

print('\n Programa que recebe o Ano de Nascimento e o ano atual \n')

anoNascimento = int(input('Digite o Ano de Nascimento: \n'))

anoAtual = int(input('Digite o ano atual: \n'))


idadeA = (anoAtual - anoNascimento) 
 
print('\nVocê tem:', idadeA, 'Anos de Idade \n')

diferenca = (2025 - anoAtual)
idadeB = (idadeA + diferenca)

print('Sua idade em 2025 seria', idadeB)