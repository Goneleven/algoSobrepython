# ATIVIDADE 7
#|Faça um programa que receba os dados de 5 produtos: preço unitário, país de origem (1 –EUA, 2 –México e 3 –outros), meio de transporte
#|(T –Terrestre, F-Fluvial e A –Aéreo), carga perigosa (S –Sim, N-Não). Calcule e mostre:

#|O valor do imposto calculado usando a tabela a seguir.

"""
Preço unitário      Percentual de impostos Sobre preço unitário

até R$ 100,00                       5%
maior do que R$ 100,00              10%

"""

#|O valor de transporte calculado usando a tabela a seguir;

"""
Carga periogosa         Pais de origem          Valor do transporte

                            1                         R$ 50,00
    S                       2                         R$ 35,00  
                            3                         R$ 24,00
                            1                         R$ 12,00
    N                       2                         R$ 35,00
                            3                         R$ 60,00

"""

#|O valor do seguro, calculado usando a regra a seguir: -Os produtos que vêm do México e os produtos que utilizam transporte aéreo pagam metade do
#|valor de seu preço unitário como seguro;
#|O preço final de cada produto;

print("\nprograma que calculca o valor de um produto" )

cont = 0

while(cont < 5):
    precoProduto = float(input('\ninsira o valor do produto: '))
    paisDeOrigem = int(input("Digite o Pais de Origem: \n1 - EUA \n2 - México \n3 - outros\n"))
    tranporteProduto = input("Digite o Transporte para o produto: \nT - Terrestre \nF - Fluvial \nA - Aéreo\n")
    cargaPerigosa = input("A Carga é perigosa? (S) para SIM | (N) para NÃO\n")
    
    # IF Do imposto do Produto:
    if(precoProduto > 100):
        precoProduto = precoProduto * 1.1
        
    else:
        precoProduto = precoProduto * 1.05
    
    # IF do Perigo|Trans do Produto
    if(cargaPerigosa == "S" or cargaPerigosa == "s"):
        if(paisDeOrigem == 1):
            precoTransporte = 50
            
        else:
            if(paisDeOrigem == 2):
                precoTransporte = 35
                precoProduto = (precoProduto / 2)
                
            else:
                if(paisDeOrigem == 3):
                    precoTransporte = 24
                    
                else:
                    print("Alguma informação não faz sentido, refaça")
        
        # Caso não tenha perigo:
    else:
        if(paisDeOrigem == 1):
            precoTransporte = 12
            
        else:
            if(paisDeOrigem == 2):
                precoTransporte = 35
                precoProduto = (precoProduto / 2)
                
            else:
                if(paisDeOrigem == 3):
                    precoTransporte = 60
                    
                else:
                    print("Alguma informação não faz sentido, refaça")
                    
    if(tranporteProduto == "A" or tranporteProduto == "a"):
        precoProduto = (precoProduto / 2)
        
    else:
        print("Pagará o valor total do Transporte")
                   
    precoTotal = (precoTransporte + precoProduto)  
    print("o Total a pagar: \n", precoTotal)
    
    cont+=1