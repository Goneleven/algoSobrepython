#Criar um algoritmo que calcule o consumo médio de um automóvel (medido em km/l),
#dado que são conhecidos a distancia total percorrida e o volume de conbustivel consimido para
#percorre-la (medido em litros).

#Atividade 3:

print('Programa para calcular o consumo médio de um automóvel (medido em km/l)')

distancia_percorrida = float(input ('Entre com a distância percorrida:'))

volume_combustível = float(input ('Entre com o volume de combustível consumido:'))

consumo = distancia_percorrida / volume_combustível 

print('o Consumo é de: ', consumo)