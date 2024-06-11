# ATIVIDADE 9
#|Elabore um algoritmo e respectivo programa em Python que realize o que se pede: - receba o nome e a nota de cada aluno(a) até receber uma informação de finalização pelo usuário;
#| - guarde estes valores em uma lista;
#| - imprima esta lista ordenada de forma crescente por nome;
#| - calcule e mostre: a média, aluno(a) com maior nota e aluno (a) com menor nota.

matrizAlunos = []
nome = ""
nota = float
infoCompletas = 0

flag = True

while flag:
    nome = input("|Digite o nome do Aluno \n|Digite (Parar) para Encerrar a Lista:\n")

    if (nome.lower() == "parar"):
        flag = False
        break

    nota = float(input("Digite a nota do Aluno:\n"))
    infoCompletas =+1

    # Armazenando os dados:
    matrizAlunos.append([nome, nota])

    # Deixando em ordem crescente por nome:
    matrizAlunos.sort()
    

# Pegando a MÉDIA Sala
media = sum(aluno[1] for aluno in matrizAlunos) / len(matrizAlunos)

# Pegando a MAIOR Nota:
maiorNota = max(aluno[1] for aluno in matrizAlunos)
maiorNotaAluno = next((aluno[0] for aluno in matrizAlunos if aluno[1] == maiorNota))

# Pegando a MENOR Nota:
menorNota = min(aluno[1] for aluno in matrizAlunos)
menorNotaAluno = next((aluno[0] for aluno in matrizAlunos if aluno[1] == menorNota))

print(f"\n| Média da SALA: {media:.1f}")
print(f"| Aluno / Maior Nota: {maiorNotaAluno} {maiorNota:.1f}")
print(f"| Aluno / Menor Nota: {menorNotaAluno} {menorNota:.1f}")

print(f"\n| Notas de todos os alunos: \n{matrizAlunos}")