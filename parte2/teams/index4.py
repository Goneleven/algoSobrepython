#ATIVIDADE 4:
#|Criar um alrotitmo que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários
#|para executor cada operação
#|
#|Menu de opções:
#|1 - Somar dois números
#|2 - Multiplicar dois números
#|3 - Subtrair dois números
#|4 - Dividir dois números



print('Algoritmo para realizar operações matematicas')

print('\n1 - Somar dois números \n2 - Multiplicar dois números \n3 - Subtrair dois números \n4 - Dividir dois números')

numeroA = int(input('Digite o PRIMEIRO número: '))
numeroB = int(input('Digite o SEGUNDO número: '))
operacao = int(input('Digite a operação desejada: '))

if(operacao == 1):
    print('\nA Soma é =', (numeroA + numeroB))
    
elif(operacao == 2):
    print('\nA Multiplicação é =', (numeroA * numeroB))
    
elif(operacao == 3):
    print('\nA Subtração é =', (numeroA - numeroB))
    
elif(operacao == 4):
    print('\nA Divisão é =', (numeroA / numeroB))
    
else:
    print('\nNão é uma operação existente, pelo menos, não no programa')