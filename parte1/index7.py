# ATIVIDADE 7
#|Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.  

print('\n Programa que calcula a média final \n')

notaA = float(input('Coloque a nota da prova A (Peso 2): '))
notaB = float(input('Coloque a nota da prova B (Peso 3): '))
notaC = float(input('Coloque a nota da prova C (Peso 5): '))

notaA = (notaA * 2)
notaB = (notaB * 3)
notaC = (notaC * 5)

media = (notaA + notaB + notaC) /10

print('\nA Média desse aluno é: ', media)