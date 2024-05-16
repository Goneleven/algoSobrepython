#Criar um algoritmo que leia o saldo de uma aplicação e imprima o novo saldo,
#considerando um reajuste de 15%

#Atividade 4:

print('Programa que calcula reajuste de 15% em uma aplicação')


#VAR

saldo = float(input('Escreva o Saldo: '))


#PROCESSAMENTO

saldoNovo = saldo * 1.15

print('O Novo saldo da aplicação é de: R$ {:.2f}'. format(saldoNovo))