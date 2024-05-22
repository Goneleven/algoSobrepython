# ATIVIDADE 4
#|Elaborar um algoritmo que simule o jogo de adivinhação: o jogador 1 escolhe um número entre 1 e 10; o jogador 2 insere números na
#|tentativa de acertar o número escolhido pelo jogador  1.  Quando  ele  acertar,  o  algoritmo  deve  informar  que  ele  acertou  o 
#|número escolhido pelo jogador 1 em x tentativas (quantidade de tentativas do jogador 2).

print("\n Programa simule um jogo de adivinhação \n")

jogadorUm = int(input("Jogador 1, insira um número de 1 a 10: "))
erros = 0

if(jogadorUm < 10 and jogadorUm > 0):
    jogadorDois = int(input("Jogador 2, adivinhe o número do jogador 1 (O número está entre 1 a 10): "))

    while(jogadorUm != jogadorDois):
        erros+=1
        print(f"Você errou em, você tem {erros} erro(s)")
        jogadorDois = int(input("Tente de novo, Acerte o número do Jogador 1: "))

    print("Parabéns! Você acertou colega!")

else:
    print("Jogador um, Esse número não pode, comece o programa de novo, e coloque outro numero")