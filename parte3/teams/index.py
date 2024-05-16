#ATIVIDADE 1:
#|Na declaração de imposto de renda devem constar os dados: nome do contribuinte, CPF, renda anual e número de dependentes.
#|Os cálculos são feitos da forma a seguir. 
#|* Desconto de R$ 110,00 por dependente. 
#|* Com base na renda líquida (renda anual menos descontos) é calculada a alíquota de contribuição de acordo com a tabela: 

print('\n Programa que calcula imposto de renda\n')

# Variavéis
nomeContribuinte = (input("Digite o nome do contribuinte: "))
cpf = int(input("Digite seu CPF, sem pontos: "))
rendaAnual = float(input("Digite sua Renda Anual: "))
numeroDeDependentes = int(input("Digite o Numero de Dependentes: "))

desconto = (numeroDeDependentes * 110)
rendaLiquida = (rendaAnual - desconto)



if(rendaLiquida <= 800):
    print(nomeContribuinte, "|", cpf, "| Você está Isento")

else:
    if(rendaLiquida >= 801 and rendaLiquida <= 4000):
        aliquota = 0.025
        print("2.5% de alíquota")
        valorImposto = (rendaLiquida * aliquota)
        print(nomeContribuinte, "|", cpf, "| Valor: ", valorImposto) 
    
    else:
        if(rendaLiquida >= 4001 and rendaLiquida <= 9000):
            aliquota = 0.05
            print("5% de alíquota")
            valorImposto = (rendaLiquida * aliquota)
            print(nomeContribuinte, "|", cpf, "| Valor: ", valorImposto) 

        else:
            aliquota = 0.1
            print("10% de alíquota")
            valorImposto = (rendaLiquida * aliquota)
            print(nomeContribuinte, "|", cpf, "| Valor: ", valorImposto) 