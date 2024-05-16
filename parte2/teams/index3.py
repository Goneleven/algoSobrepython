#ATIVIDADE 3
#| criar um algoritmo que leia a idade de uma pessoa e informar a sua classe eleitoral:
#| a - Não eleitor (abaixo de 16 anos)
#| b - Eleitor obrigatório (entre 18 e 65 anos)
#| c - Eleitor facultativo (entre 16 e 18 ou maior que 65 anos)

print('Algoritmo para exibir sua classe Eleitoral')


idade = int(input('\nInforme a sua idade VERDADEIRA: '))

if(idade < 16 and idade >= 0):
    print('Não pode votar')
    
    
elif(idade >= 18 and idade <= 65):
    print('Você tem que votar')
    
    
elif(idade >= 16 and idade < 18 or idade > 65 and idade < 111):
    print('Se quiser pode votar ai')
    
else:
    print('invalido')