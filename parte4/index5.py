# ATIVIDADE 5
#|Uma fábricatem  uma  linha  de  produção  capaz  de  produzir  400  peças  /  dia.  Um funcionário controla a qualidade, 
#|cadastrando o número da peça e o seu estado (aprovado ou  reprovado).  Criar  um  algoritmo  para  cadastrar  o  controle  de
#|qualidade,  imprimir  os números das peçasreprovadas, e o total de peças aprovadas e reprovadas no final do dia.

print('\nprograma que serve para controle de qualidade de peças de um fábrica\n') 

total_Pecas = 400 

pecas_aprovadas = 0 

pecas_reprovadas = 0 

for i in range(0,total_Pecas,1): 

    estado = (input('insira o estado da peça (aprovado ou reprovado): ')) 

 

    if(estado == 'reprovado'): 

        pecas_reprovadas += 1 

 

    elif(estado == 'aprovado'): 

        pecas_aprovadas += 1 

 

    else:  

        print('estado inexistente') 

        i -= 1 

print('\nRELATÓRIO FINAL\n') 

print(f'houve um total de {pecas_aprovadas} aprovadas') 

print(f'houve um total de {pecas_reprovadas} aprovadas') 