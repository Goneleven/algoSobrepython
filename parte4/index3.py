# ATIVIDADE 3
#|Supondo que a população de um país A seja da ordem de 98.000.000 de habitantes, com uma  taxa  anual  de  crescimento  de  3,5% 
#|e  que  um  país  B  tenha  uma  população  de aproximadamente 200.000.000 habitantes com uma taxa anual de crescimento de 1,5%.
#|Escreva  um  algoritmo  que  calcule  iterativamente,  quantos  anos  serão  necessários  para que a população do país A, ultrapasse ou
#|iguale a população do país B, mantidas as taxas de crescimento.

print('\nprograma que calcula taxa de crescimento de um país\n') 

paisA = 98000000 

paisB = 200000000 

anos = 0 

while(paisA <= paisB): 

    paisA += paisA * 0.035 

    paisB += paisB * 0.015 

    anos+=1 

print(f'o país A alcançará o país B em {anos} anos\n') 