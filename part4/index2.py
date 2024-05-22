# ATIVIDADE 2
#|Criar  um  algoritmo  que  deixe  escolher  qual  a  tabuada  de  multiplicar  que  se  deseja imprimir.

print("\n Programa que deixa escolher a tabuada \n")

numeroVezes = int(input("Coloque a tabuada desejada: "))
contador = 1

while (contador <= 10):
    print(f'{numeroVezes} x {contador} =', numeroVezes * contador)
    contador+=1  