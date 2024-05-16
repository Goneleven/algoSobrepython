#ATIVIDADE 2
#|Criar um algoritmo que receba o código correspondente ao cargo de um funcionário e mostre o cargo
#|1 - Escriturário
#|2 - Secretária
#|3 - Caixa
#|4 - Gerente
#|5 - Diretor

print('Algoritmo para exibir o cargo correspondente')

numeroSeletor = int(input('Digite seu número de funcionário: '))

if(numeroSeletor == 1):
    print('Olá Escriturário')
    
elif(numeroSeletor == 2):
    print('Olá Secretária')
    
elif(numeroSeletor == 3):
    print('Olá Caixa')
    
elif(numeroSeletor == 4):
    print('Olá Gerente')
    
elif(numeroSeletor == 5):
    print('Olá Diretor')
    
else:
    print('Você não trabalha aqui, eu acho')