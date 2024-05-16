# ATIVIDADE 3
#|Criar um algoritmo que converta segundos em minutos e segundos. Por exemplo, 252 segundos equivalem a 4 minutos e 12 segundos. 

print('\n Programa que transforma SEGUNDOS em MINUTOS \n')

segundos = int(input('Escreva um tempo em SEGUNDOS \n'))

if(segundos >= 60):
    minutos = int(segundos/60)
    segundosB = (segundos % 60)
    print('{:.0f}'.format(minutos), 'Minuto(s)', 'e', segundosB, 'Segundo(s)')

else:
    print(segundos, 'Segundo(s)')