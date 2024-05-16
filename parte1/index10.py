# ATIVIDADE 10
#|João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as contas estão atrasadas, João terá que pagar multa de 2% sobre cada conta.
#|Faça um algoritmo que calcule e mostre quanto restará do salário do João. 

print('\n Programa que calcula multa de duas Contas \n')

salario = float(input('digite seu salario: '))

conta1 =  float(input('\ndigite o valor da PRIMEIRA conta: '))

conta2 = float(input('\ndigite o valor da SEGUNDA conta: '))


imposto1 = conta1 * 1.02

imposto2 = conta2 * 1.02 

totalSalario = salario - (imposto1 + imposto2)

print("\nQuanto sobrou do seu Salário: R$", totalSalario)