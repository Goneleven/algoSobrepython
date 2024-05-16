#Criar um algoritmo que receba o salário de um funcionário e o percentual de aumento,
#calcule e mostre o valor do aumento e o novo salário. 

#Atividade 5:

print('Programa que calcula o reajuste salarial de acordo com percentual de aumento')

#VAR

salario = float(input('Coloque o salário Legal :D \n'))

aumentoPercentual = float(input('Coloque o percentual de aumento: \n'))

#EXEC.

aumento = salario * (aumentoPercentual / 100)

salarioNovo = salario + aumento

print('O Novo salario é de: R$ {:.2f}'.format(salarioNovo))
print('Aumento no salário de: {:.2f}'.format(aumento))