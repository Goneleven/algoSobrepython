#ATIVIDADE 1
#|Construa um algoritmo que leia 3 valores inteiros e positivos e encontre o menor e o maior valor e calcule a média dos 3 número lidos

print('\n Programa que mostra o valor maior e menor, e calcula a média\n')

numeroA = int(input("Escreva o primeiro numero: "))
numeroB = int(input("Escreva o segundo numero: "))
numeroC = int(input("Escreva o terceiro numero: "))

maiorNumero = int
menorNumero = int

#Achar o maior e menor numero:
if((numeroA > 0) and (numeroB > 0) and (numeroC > 0)):
    if(numeroA > numeroB > numeroC):
        maiorNumero = numeroA
        menorNumero = numeroC

    else:
        if(numeroA > numeroC > numeroB):
            maiorNumero = numeroA
            menorNumero = numeroB

        else:
            if(numeroB > numeroA > numeroC):
                maiorNumero = numeroB
                menorNumero = numeroC

            else:
                if(numeroB > numeroC > numeroA):
                    maiorNumero = numeroB
                    menorNumero = numeroA

                else:
                    if(numeroC > numeroA > numeroB):
                        maiorNumero = numeroC
                        menorNumero = numeroB

                    else:
                        maiorNumero = numeroC
                        menorNumero = numeroA
    #Calcular média:
    media = (numeroA + numeroB + numeroC) / 3

    #Resultado:
    print("\n| A Média é: {:.2f}".format(media))
    print("| O Maior número é:", maiorNumero)
    print("| O Menor número é:", menorNumero)

else:
    print("Você colocou um ou mais números menores ou iguais a 0")
    
