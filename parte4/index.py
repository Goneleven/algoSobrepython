# ATIVIDADE 1
#|Criar um algoritmo que leia a idade de 1000 pessoas. Exiba a quantidade de pessoas em cada classe eleitoral:
#|Não-eleitor (abaixo de 16 anos)
#|Eleitor obrigatório (entre 18 e 65 anos)
#|Eleitor facultativo (entre 16 e 18 e maior de 65 anos)

print("\n Programa que identifica se é eleitor ou não\n")

pessoas = 0

while (pessoas <= 1000):
    idade = int(input("Coloque a sua IDADE: "))

    if(idade < 16):
        print("Você não tem idade para ser eleitor")

    else:
        if(idade >= 18 and idade <= 65):
            print("Você tem idade suficiente e terá que votar")

        else:
            print("Você é Eleitor Facultativo")


    pessoas+=1
