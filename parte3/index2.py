#ATIVIDADE 2
#|Escreva um algoritmo que determine o grau de obesidade de uma pessoa sendo fornecido o peso e a altura da pessoa,
#|o grau de obesidade é determidado pelo indice da massa corporea (Massa = peso / altura²) através da tabela abaixo:
#| MASSA CORPÓREA      -       GRAU DE OBESIDADE
#     <26                         NORMAL
#     >= 26 e <30                 OBESO
#     >= 30                       OBESO MÓRBIDO
import math

print('\n Programa que calcula Massa Corpórea e mostra grau de obesidade\n')

peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a Sua altura: "))

massa = (peso/(altura * altura))

if(massa < 26):
    print("\nVocê está com o peso ideal")

else:
    if(massa >= 26 and massa < 30):
        print("\nVocê é obeso")

    else:
        if(massa >= 30):
            print("\nVocê é Obeso Mórbido")

        else:
            print("\nDados não fazem sentido")

print("Seu IMC é de:", massa)