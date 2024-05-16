#ATIVIDADE 1:
#|Criar um algoritmo que receba a média de um aluno e mostre a situação:
#|a - Aprovado -> média >= 5
#|b - Exame -> Média entre 3 e 5
#|c - Reprovado -> Média menor do que 3

print('Algoritmo para calcular a média')

mediaAluno = float(input('Informe a Média: '))

if(mediaAluno >= 5 and mediaAluno <= 10):
    print('APROVADO')
    
    
elif(mediaAluno >= 3 and mediaAluno < 5 ):
    print('Você está de exame mocinho')
    
    
elif(mediaAluno < 3 and mediaAluno >= 0):
    print('Reprovado')
    
    
else:
    print('Média invalida')