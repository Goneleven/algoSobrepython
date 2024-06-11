# ATVIDADE 7
#|Elaborar um programa em Python que leia os nomes e telefones de 20 pessoas e armazene numa lista. A partir de uma consulta por nome, o programa deverá mostrar o NOME e TELEFONE da pessoa. 

agenda = {}

#recebendo os nomes e os numeros de telefone 

for i in range (20):
    nome = input("Digite o nome {}ª pessoa: ".format(i+1))
    telefone = input("Digite o telefone {}: ".format (nome))
    agenda[nome] = telefone 
  
#consulta por nome 

consulta = input("Digite o nome da pessoa que deseja consultar: ")

#Verificação do nome consultado esta aparecendo junto com o telefone

if (consulta in agenda): 
    print("telefone de {}:{}".format(consulta, agenda[consulta]))

else: 
    print("Nome não está na agenda.")