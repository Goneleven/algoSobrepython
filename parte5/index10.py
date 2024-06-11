# ATIVIDADE 10
#| Matrizes multidimensionais são vetores capazes de armazenarem mais de uma posição de cada elemento que será indicado por dois ou mais índices. Um exemplo de matrizes
#| multidimensionais são as matrizes matemáticas, que representam valores tabulados em linhas e colunas. 
"""
Considerando o algoritmo acima e com base no teste de mesa, faça o que se pede nos itens a seguir: 
a)      Apresente os dados dos vetores m1 e m2 ao término da execução da linha 12 
M1 =  [[1, 1, 1], [2, 2, 2], [3, 3, 3]] 
M2 =  [[1, 2, 3], [1, 2, 3], [1, 2, 3]] 
b)     Apresente os dados dos vetores m1 e m2 ao término da execução da linha 21 
M1 =  [[0, 1, 1], [2, 0, 2], [3, 3, 0]] 
M2 =  [[1, 1, 1], [1, 2, 1], [1, 1, 3]] 
"""

# Inicialização das matrizes m1 e m2
m1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
m2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Processamento das matrizes
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if i == j:
            m1[i][j] = 0
        else:
            m2[i][j] = m1[i][j]

# Impressão das matrizes
print("M1 =", m1)
print("M2 =", m2)